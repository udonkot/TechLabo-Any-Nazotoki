from typing import List, Optional
from app.config.stage_config import STAGE_CONFIGS
from app.models.stage import StageConfig


class StageService:
    """ステージ情報の取得・管理サービス（CLI / Web 共通）"""

    def get_all(self) -> List[StageConfig]:
        return STAGE_CONFIGS

    def get_by_id(self, stage_id: int) -> Optional[StageConfig]:
        return next((s for s in STAGE_CONFIGS if s.id == stage_id), None)

    def get_problem_file(self, stage_id: int, language: str) -> Optional[str]:
        stage = self.get_by_id(stage_id)
        if stage is None:
            return None
        return stage.problem_files.get(language)
