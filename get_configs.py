import itertools
import numpy as np
import os


def get_random_configs():
  n_samples = 576
  rng_seed = 202204041708
  align_split = [8, 12, 16, 20, 24, 32, 48, 72]
  optimize_split = [8, 12, 16, 20, 24, 32, 48, 72]
  optimize_reps = [1, 2, 3, 4, 5]
  cuda_threads = [32, 64, 96, 128, 160, 192, 224, 256]
  num_restarts = [256, 1024]
  clipping = [10, 30, 50, 256]  # 1024
  similarity_thresh = [1, 2, 3, 4]
  buffer_size = [1048576, 2097152, 5242880, 10485760, 20971520, 52428800]
  parser_workers = [20]  # [2, 4, 8, 10, 20]
  bucketizer_workers = [4]  # [1, 2, 4, 5, 10]
  dock_score_workers = [6]  # [2, 4, 6, 8]
  parameter_space = [align_split, optimize_split, optimize_reps, cuda_threads,
                     num_restarts, clipping, similarity_thresh, buffer_size,
                     parser_workers, bucketizer_workers, dock_score_workers]

  n_tot = np.prod([len(l) for l in parameter_space])
  rng = np.random.default_rng(rng_seed)
  samples_idxs = rng.choice(range(n_tot), size=n_samples, replace=False)
  with open(os.path.join('datasets', 'configs01.txt'), 'w') as f:
    for i, config in enumerate(itertools.product(*parameter_space)):
      if i % 10000 == 0:
        print(i)
      if i in samples_idxs:
        strg = ' '.join([str(_) for _ in config]) + '\n'
        f.write(strg)


def get_fixed_configs():
  align_split = [8, 16]
  optimize_split = [8, 24]
  optimize_reps = [1, 3, 5]
  cuda_threads = [32, 96]
  num_restarts = [256, 1024]
  clipping = [10, 50, 256]
  similarity_thresh = [1, 2, 3, 4]
  buffer_size = [1048576, 5242880]
  parser_workers = [20]
  bucketizer_workers = [4]
  dock_score_workers = [6]
  parameter_space = [align_split, optimize_split, optimize_reps, cuda_threads,
                     num_restarts, clipping, similarity_thresh, buffer_size,
                     parser_workers, bucketizer_workers, dock_score_workers]
  n_tot = np.prod([len(l) for l in parameter_space])

  with open(os.path.join('datasets', 'configs02.txt'), 'w') as f:
    for config in itertools.product(*parameter_space):
      strg = ' '.join([str(_) for _ in config]) + '\n'
      f.write(strg)
  print("Wrote", n_tot, "configurations")


def get_all_configs():
  align_split = [8, 12, 16, 20, 24, 32, 48, 72]
  optimize_split = [8, 12, 16, 20, 24, 32, 48, 72]
  optimize_reps = [1, 2, 3, 4, 5]
  cuda_threads = [32, 64, 96, 128, 160, 192, 224, 256]
  num_restarts = [256, 1024]
  clipping = [10, 30, 50, 256]  # 1024
  similarity_thresh = [1, 2, 3, 4]
  buffer_size = [1048576, 2097152, 5242880, 10485760, 20971520, 52428800]
  parser_workers = [20]  # [2, 4, 8, 10, 20]
  bucketizer_workers = [4]  # [1, 2, 4, 5, 10]
  dock_score_workers = [6]  # [2, 4, 6, 8]

  parameter_space = [align_split, optimize_split, optimize_reps, cuda_threads,
                     num_restarts, clipping, similarity_thresh, buffer_size,
                     parser_workers, bucketizer_workers, dock_score_workers]

  with open(os.path.join('datasets', 'configs_all.csv'), 'w') as f:
    f.write(('ALIGN_SPLIT,OPTIMIZE_SPLIT,OPTIMIZE_REPS,CUDA_THREADS,N_RESTART,'
             'CLIPPING,SIM_THRESH,BUFFER_SIZE,WORKER_PARS,WORKER_BUCK,'
             'WORKER_DS\n'))
    for config in itertools.product(*parameter_space):
      f.write(','.join([str(_) for _ in config]) + '\n')


if __name__ == '__main__':
  pass
  get_all_configs()
