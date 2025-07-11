# Project: Visual Command Agent

### Project Overview

THis project simulates a real-world AI infrastructure. It covers the full lifecycle of developing, profiling, and deploying a vision-language model using PyTorch and Azure ML.

A model that can see an image, interpret a user's natural language instruction, and perform a simulated action (like pointing, describing, or planning movement)

# Visual Command Agent - AI Infrastructure Project

#### Project Structure

|--- training/

    |--- model.py      # PyTorch model: vision-language encoder-decoder

    |---  train.py        # Training loop using PyTorch

    |---  dataset.py   # Custom dataset for images + commands

    |--- config.yaml   # Config for training parameters

|--- profiling/

    |--- profiler.py     # PyTorch profiler script

    |--- analysis.md   # Results + optimization notes

|--- scripts/

    |--- setup_env.sh     # Bash script for environment setup

    |--- monitor_gpu.sh    #Live GPU/CPU/mem monitoring

    |--- azure_submit.py   # Azure ML job submission script

|--- docs/

    |--- project_overview.md    # system design, goals, behavior prep

|--- README.md
