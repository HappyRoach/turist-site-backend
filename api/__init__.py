from fastapi import APIRouter
from .endpoints import user, role, auth, destination, tour

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(role.router, prefix="/roles", tags=["roles"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(destination.router, prefix="/destinations", tags=["destinations"])
router.include_router(tour.router, prefix="/tours", tags=["tours"])