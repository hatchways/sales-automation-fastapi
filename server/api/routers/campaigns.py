from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm.session import Session

from api import schemas
from api.dependencies.auth import get_current_user
from api.core.constants import DEFAULT_PAGE, DEFAULT_PAGE_SIZE
from api.crud import CampaignCrud, ProspectCrud
from api.dependencies.db import get_db

router = APIRouter(prefix="/api", tags=["campaigns"])


@router.get("/campaigns", response_model=schemas.CampaignResponse)
def get_campaign_page(
    current_user: schemas.User = Depends(get_current_user),
    page: int = DEFAULT_PAGE,
    page_size: int = DEFAULT_PAGE_SIZE,
    db: Session = Depends(get_db),
):
    """Get a single page of campaigns"""
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Please log in"
        )
    campaigns = CampaignCrud.get_users_campaign(db, current_user.id, page, page_size)
    total = CampaignCrud.get_user_campaign_total(db, current_user.id)
    return {"campaigns": campaigns, "size": len(campaigns), "total": total}
