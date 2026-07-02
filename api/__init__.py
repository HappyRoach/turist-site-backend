from fastapi import APIRouter
from .endpoints import user, role, auth, destination, tour, direction, survey, setting

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(role.router, prefix="/roles", tags=["roles"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(destination.router, prefix="/destinations", tags=["destinations"])
router.include_router(tour.router, prefix="/tours", tags=["tours"])
router.include_router(direction.router, prefix="/directions", tags=["directions"])
router.include_router(survey.router, prefix="/survey", tags=["survey"])
router.include_router(setting.router, prefix="/settings", tags=["settings"])