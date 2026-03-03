from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class StageConfig:
    """ステージ設定モデル（CLI / Web 共通）"""
    id: int
    title: str
    description: str
    fragment_label: str
    answer: str
    hints: List[str] = field(default_factory=list)
    problem_files: dict = field(default_factory=dict)  # {"python": "path", "java": "path"}
    max_attempts: int = 3


@dataclass
class StageResult:
    """ステージ実行結果モデル"""
    stage_id: int
    cleared: bool
    fragment: Optional[str] = None
    attempts_used: int = 0
