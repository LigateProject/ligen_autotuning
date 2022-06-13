import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

# plt.style.use('dark_background')


def obj_func(datum):
  """TIME*AVG_RMSD^2"""
  return datum['AVG_RMSD'] ** 2 * datum['TIME']


def read_df(file):
  file_path = os.path.join('datasets', file)
  df = pd.read_csv(file_path)
  df[obj_func.__doc__] = df.apply(obj_func, axis=1)
  name = file.replace('.csv', '')
  metrics = 'TIME,THROUG,AVG_RMSD'.split(',') + [obj_func.__doc__]
  return df, name, metrics


def scatter_metrics(file, description, single_configs={}):
  """
  single_configs is a dict: str -> tuple, where str is the filename and tuple
  contains the label and the color
  """

  df, df_name, _ = read_df(file)
  met1 = 'THROUG'
  met2 = 'AVG_RMSD'

  fig, ax = plt.subplots()
  ax.scatter(df[met1], df[met2], label='points')
  ax.set_xlabel(met1)
  ax.set_ylabel(met2)
  ax.set_title(f"{df_name} - {description} - size: {df.shape[0]}")

  if single_configs:
    for config_file, (desc, col) in single_configs.items():
      df_config, _, _ = read_df(config_file)
      ax.scatter(df_config[met1], df_config[met2], label=desc, color=col)
    ax.legend(loc='upper right')

  plt.savefig(os.path.join('plots', f'scatter_{df_name}.png'), dpi=300,
              bbox_inches='tight')


def hist_metrics(file, description, single_configs={}):
  """
  See scatter_metrics()
  """
  df, df_name, metrics = read_df(file)

  fig, axes = plt.subplots(1, 4, figsize=(26, 8))
  for i, metric in enumerate(metrics):
    vals = df[metric]
    mean = vals.mean()
    std = vals.std()
    ax = axes[i]
    ax.hist(vals, label='data')
    ax.axvline(mean, color='red', label='mean')
    ax.axvline(mean-std, color='red', ls='--', label='std')
    ax.axvline(mean+std, color='red', ls='--')

    if single_configs:
      for config_file, (desc, col) in single_configs.items():
        df_default, _, _ = read_df(config_file)
        ax.axvline(float(df_default[metric]), label=desc, color=col)

    ax.set_title(metric)
    ax.legend(loc='upper right')

  fig.suptitle(f"{df_name} - {description} - size: {df.shape[0]}")
  plt.savefig(os.path.join('plots', f'hist_{df_name}.png'), dpi=300,
              bbox_inches='tight')


def plot_objective_by_iteration(file, description):
  # Get DataFrame
  file_path = os.path.join('datasets', file)
  df = pd.read_csv(file_path)
  df_name = file.rstrip('.csv')

  # Compute values of objective function for each data point
  obj_vals = df.apply(obj_func, axis=1)
  
  # Plot values
  fig, ax = plt.subplots(figsize=(10, 4))
  ax.plot(obj_vals, marker='.')
  ax.grid(axis='y')
  offset = 10
  ax.set_xlim((min(df.index)-offset, max(df.index)+offset))
  ax.set_xticks(np.arange(0, max(df.index)+offset, 10), minor=True)
  ax.set_xlabel("iteration")
  ax.set_ylabel(obj_func.__doc__)
  ax.set_title(f"{df_name} - {description} - size: {df.shape[0]}")
  fig.savefig(os.path.join('plots', f'objective_{df_name}.png'),
              bbox_inches='tight', dpi=300)


def plot_regret(file, description, optimal_y=None, percent=False):
  file_path = os.path.join('datasets', file)
  df = pd.read_csv(file_path)
  df_name = file.rstrip('.csv')

  df_obj = df.apply(obj_func, axis=1)
  if optimal_y is None:
    optimal_y = np.min(df_obj)
  incumbents = np.minimum.accumulate(df_obj)
  regrets = incumbents - optimal_y
  if percent:
    regrets = 100 * regrets / optimal_y

  fig, ax = plt.subplots(figsize=(10, 4))
  ax.grid(axis='y')
  ax.plot(regrets, marker='.')
  offset = 10
  ax.set_xlim((min(df_obj.index)-offset, max(df_obj.index)+offset))
  ax.set_xticks(np.arange(0, max(df_obj.index)+offset, 10), minor=True)
  ax.set_xlabel("iteration")
  ax.set_ylabel("regret (%)" if percent else "regret")
  ax.set_title(f"{df_name} - {description} - size: {df_obj.shape[0]}")
  fig.savefig(os.path.join('plots', f'regrets_{df_name}.png'),
              bbox_inches='tight', dpi=300)


if __name__ == '__main__':
  single_configs = {
    'ligen00_default.csv': ('default', 'orange')
  }
  datasets = {
    'ligen01.csv': 'random configurations',
    'ligen02.csv': 'grid search'
  }
  for data, desc in datasets.items():
    hist_metrics(data, desc, single_configs=single_configs)
    scatter_metrics(data, desc, single_configs=single_configs)
