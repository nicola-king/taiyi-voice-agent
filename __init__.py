# 太一语音 Agent 全域自进化智能体

> **版本**: v5.0 (全域自进化版)  
> **创建时间**: 2026-04-15  
> **作者**: 太一 AGI  
> **许可**: MIT

"""
太一语音 Agent 全域自进化智能体

核心能力:
1. 全网语音技术学习 - 博主/开源项目/论文/报告
2. 知识蒸馏 - 提取语音技术/模型/优化方案
3. 语音识别进化 - ASR 模型优化 (+5%/代)
4. 语音合成进化 - TTS 模型优化 (+5%/代)
5. 情感语音进化 - 情感化 TTS 优化 (+6%/代)
6. 模型进化 - 语音模型持续优化 (+5%/代)
7. 递归优化 - 反馈收集/迭代优化
"""

from .core import VoiceAgent, LearningEngine, EvolutionEngine, ApplicationEngine

__version__ = "5.0.0"
__all__ = [
    "VoiceAgent",
    "LearningEngine",
    "EvolutionEngine",
    "ApplicationEngine"
]
