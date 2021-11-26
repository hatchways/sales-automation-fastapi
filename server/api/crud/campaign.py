from typing import List, Union
from sqlalchemy.orm.session import Session
from api import schemas
from api.models import Campaign
from api.core.constants import DEFAULT_PAGE_SIZE, DEFAULT_PAGE, MIN_PAGE, MAX_PAGE_SIZE

MAX_SEARCH_RESULTS = 10


class CampaignCrud:
    @classmethod
    def get_users_campaign(
        cls,
        db: Session,
        user_id: int,
        page: int = DEFAULT_PAGE,
        page_size: int = DEFAULT_PAGE_SIZE,
    ) -> Union[List[schemas.Campaign], None]:
        """Get user's campaigns"""
        if page < MIN_PAGE:
            page = MIN_PAGE
        if page_size > MAX_PAGE_SIZE:
            page_size = MAX_PAGE_SIZE
        res = (
            db.query(Campaign)
            .filter(
                Campaign.user_id == user_id,
            )
            .offset(page * page_size)
            .limit(page_size)
            .all()
        )
        return res

    @classmethod
    def get_user_campaign_total(cls, db: Session, user_id: int) -> int:
        return db.query(Campaign).filter(Campaign.user_id == user_id).count()
