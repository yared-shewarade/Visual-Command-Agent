### Profiling summary

- Observed low GPU utilization on batch sizes < 8
- Bottleneck: GRU layer shows high latency
- Recommendation: Replace GRU with transformer encoder for performance
