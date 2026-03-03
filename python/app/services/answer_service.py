from app.models.stage import StageConfig


class AnswerService:
    """答え合わせサービス（CLI / Web 共通）"""

    def check(self, stage: StageConfig, user_input: str) -> bool:
        """正規化して比較（大文字小文字・前後空白を無視）"""
        return user_input.strip().lower() == stage.answer.strip().lower()
