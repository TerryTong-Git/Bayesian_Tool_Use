---
name: astra-architecture
description: Use when adding new tasks, pressure families, or metrics to Astra; when understanding how components interact; when modifying runner, serialization, or dataset loading code
---

# Astra System Architecture

## Overview

Astra encapsulates three variable dimensions—**task**, **pressure**, and **metrics**—while keeping serialization, runner plumbing, and dataset loading stable and reusable. Any task, pressure family, or metric can be swapped without touching runners or serialization.

## Directory Conventions

| Component | Location | Notes |
|-----------|----------|-------|
| Tasks | `src/task/<task_id>/` | Interface in `src/task/__init__.py` |
| Pressure | `src/pressure/<pressure_id>/` | Interface in `src/pressure/__init__.py` |
| Metrics | `src/metrics/<metric_id>/` | Interface in `src/metrics/__init__.py` |
| Core | `src/core/` | Runner, serialization, dataset loaders |

**Organization rule:** Each directory uses subfolders for specific implementations. Interface defined in `__init__.py`. No other files except subfolders (core is the exception).

## Interfaces

### Task Interface

Owns all prompt construction and side-task handling.

```python
task.id / task.name              # Stable identifier
task.prepare(sample)             # -> TaskContext (question, choices, side_task)
task.build_arm_prompts(context, pressure_level)  # -> {baseline_prompt, intervention_prompt}
task.build_monitor_prompt(context, arm_prompts)  # -> monitor_prompt
task.outputs_parser(...)         # Optional: normalize model/monitor outputs
```

### Pressure Interface

Defines available pressure levels only. Never builds prompts directly.

```python
pressure.id                      # Stable identifier (none, mild, strong)
pressure.levels()                # -> Iterable[PressureLevel]
```

Tasks may read level descriptors to condition prompts, but pressure objects never embed prompt text.

### Metrics Interface

Consumes serialized rows and emits scores. Pure function over data.

```python
metric.id                        # Stable name
metric.compute(rows)             # -> MetricResult (no prompting or I/O)
```

Inputs: baseline/intervention Y/Z, prompts, side-task metadata. Outputs: typed result object.

## Interaction Flow

1. **Dataset -> Task**: Record parsed into `TaskContext`
2. **Pressure selection**: Runner selects `PressureLevel`
3. **Prompting**: Task renders baseline/intervention prompts
4. **Execution**: Runner sends to model/monitor, collects outputs
5. **Serialization**: One symmetric row (metadata + both arms + monitor outputs)
6. **Metrics**: Computed from serialized rows, no task/pressure branching

## Core Invariants

- **SerializedResult**: One row per datapoint with shared metadata + both arms + monitor outputs + Y/Z flags + side-task
- **Runner contracts**: Batch runner asks task for prompts, sends to model/monitor, writes row. No special casing.
- **Dataset shape**: Core loaders map records into task context. No schema changes for new components.

## Encapsulation Rules

| Component | Owns | Does NOT do |
|-----------|------|-------------|
| Tasks | Prompt templates, side-task semantics | Read from pressure/metrics internals |
| Pressure | Levels and descriptors | Build prompts, make model calls |
| Metrics | Scoring normalized data | Reach into task/pressure classes |

## Extending the System

**Add a task:**
1. Create `src/task/<task_id>/` folder
2. Implement interface methods in module
3. Supply prompt templates and parsers
4. Existing runner/serialization/metrics work unchanged

**Add a pressure family:**
1. Create `src/pressure/<pressure_id>/` folder
2. Expose new set of levels
3. Tasks optionally react to descriptors
4. Runner logic unchanged

**Add a metric:**
1. Create `src/metrics/<metric_id>/` folder
2. Implement `compute` over serialized rows
3. Register with metrics runner
4. No prompt or pressure changes needed

## Quick Reference

```
src/
  task/
    __init__.py          # Task interface
    <task_id>/           # Task implementations
  pressure/
    __init__.py          # Pressure interface
    <pressure_id>/       # Pressure implementations
  metrics/
    __init__.py          # Metrics interface
    <metric_id>/         # Metric implementations
  core/
    runner.py            # Batch runner
    serialization.py     # SerializedResult schema
    dataset.py           # Dataset loaders
```

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Pressure building prompts | Move prompt logic to task; pressure only provides levels |
| Metrics depending on task types | Use only normalized fields from SerializedResult |
| Task reaching into pressure internals | Read only the PressureLevel descriptor |
| Adding files outside subfolders | Create subfolder for new implementation |
