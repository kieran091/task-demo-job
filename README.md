# task-demo-job

一个符合 Worklane `task/v1` 约定的最小 Python Job 示例。

## 行为

任务读取 `TASK_COUNT`（默认 `3`），逐条输出处理进度并以退出码 `0` 完成。非法值会以非零退出码结束，适合验证 Job 的失败与重试策略。

## 本地运行

```bash
python3 app/job.py
TASK_COUNT=5 python3 app/job.py
```

构建入口由根目录的 `worklane.yaml` 声明，使用 `app/job.py` 和 Dockerfile。部署到 Job 时，Worklane 应引用构建生成的不可变 Package Version。
