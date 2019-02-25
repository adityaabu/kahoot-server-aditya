from flask import Blueprint
from pathlib import Path

router = Blueprint('router',__name__)

baseLocation = Path(__file__).absolute().parent.parent

from .userRoutes import *
from .questionsRoutes import *
from .quizzesRoutes import *
from .gamesRoutes import *
