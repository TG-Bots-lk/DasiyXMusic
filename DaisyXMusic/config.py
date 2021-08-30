# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("BQDFoyIjZBbQJnYi_urPH3dSmYa0Pt9c-vYPgBYqFyiPeTvaqjCEkuEnFt6j-_oAYHaIs5o8w7NBx8gjiaB7y_RZe9st7sgYCv9Fcx0utRgxnMD3-A8uONaAZBW1_3T62FutX-D4Ya1R8JlhAouQZfujWpe6kBHuGFYJ9nlUQWcYdH3NI1PEUwN3zIPwnUd0IaFfy02tnXkz6g6BKHj_da7zo4ovBC4iBaPuR9dJDw0_5by9bEqYP3Z_0pCu1smqU5yRswSp2qH8QmADgexCYv7eoDWbUZVsmmItM5V32aB-Vj_4DP-s_nC6Bar1EK_PClY7W_UyfxRjiezFw2mQvMcpI6aAA")
BOT_TOKEN = getenv("1995648542:AAEFMUfZbUZiXzoXwmVTF1b7Qg_KHl_vtoQ")
BOT_NAME = getenv("SL Song Player")
UPDATES_CHANNEL = getenv("tgbotslk")
BG_IMAGE = getenv("https://telegra.ph/file/cd2f8acb5e54d589fa065.jpg")
admins = {}
API_ID = int(getenv("7371425")
API_HASH = getenv("b569b2b80efd25a4f112a4d14bd2ec2e")
BOT_USERNAME = getenv("SongPlayerLk_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME")
SUPPORT_GROUP = getenv("tgbotslkgroup")
PROJECT_NAME = getenv("SL SONG PLAYER")
SOURCE_CODE = getenv("https://github.com/TG-Bots-lk/DasiyXMusic")
DURATION_LIMIT = int(getenv("10")
ARQ_API_KEY = getenv("VHWWWU-MDKTOL-KYXSYQ-VAVSPS-ARQ", None)
PMPERMIT = getenv("DISABLE", None)
LOG_GRP = getenv("", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("1935795880 1177233175").split()))
