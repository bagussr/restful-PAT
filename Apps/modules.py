from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile, Request, Body
from fastapi.responses import JSONResponse
from typing import List, Optional
from aiofiles import open

import os
import pathlib
import datetime
import json
