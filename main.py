import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SUDO = int(os.environ.get("SUDO","5359109940"))
Heroku = os.environ.get("HEROKU", "APP-NAME")
APP_URL = "https://"+ Heroku +".herokuapp.com/" + BOT_TOKEN
from flask import Flask, request
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

ban = ['I_W_T','N_Y_B','K_M_E','B_I_X','W_O_R',
       'O_K_G','K_S_H','G_L_J','A_S_S','U_H_B',
       'F_L_G','A_A_C','W_D_V','F_O_F','B_J_O',
       'X_E_S','K_T_W','P_Y_Q','V_B_B','S_B_W',
       'T_C_N','T_P_J','H_U_I','W_I_R','U_H_B',
       'W_O_R','H_D_X','N_Y_B','B_I_O','E_K_W',
       'D_X_V','R_I_K','C_N_C','C_F_Y','A_E_G',
       'C_H_T','O_M_T','Y_W_J','A_A_C','B_X_J',
       'U_G_C','X_N_S','Y_S_R','E_Q_C','H_K_E',
       'B_X_Z','D_D_W','X_E_S','B_X_Z','B_D_L',
       'A_F_T','D_X_V','X_C_Z','I_G_T','I_W_T',
       'X_W_V','H_V_R','X_S_I','K_S_U','E_J_Q',
       'P_G_N','U_X_O','B_X_B','W_U_B','T_P_J',
       'D_S_O','R_G_C','Q_U_W','E_T_U','F_C_T',
       'K_Q_N','U_D_B','Q_A_U','D_J_X','R_I_Q',
       'B_V_N','Q_D_W','T_J_Y','W_D_V','B_X_C',
       'Y_W_J','T_P_V','T_D_T','D_S_O','I_F_M',
       'X_N_P','Q_U_W','Q_D_O','X_D_M','Q_A_U',
       'Q_U_W','X_N_G','H_U_I','U_E_A','H_H_A',
       'D_U_Q','V_R_U','I_S_B','Y_W_P','D_Q_P',
       'X_N_S','P_V_X','L_B_D','D_J_X','G_Y_P',
       'Z_X_P','F_F_W','O_M_T','S_Y_Q','G_W_I',
       'S_G_T','N_N_J','I_H_Y','B_V_N','P_I_F',
       'V_T_G','I_V_S','J_G_L','B_I_X','R_I_Q',
       'R_G_C','K_S_H','C_F_Y','K_U_F','K_Z_U',
       'W_W_L','D_K_B','B_I_X','P_H_G','Q_C_E',
       'S_X_X','X_X_S','Q_U_H','Y_J_X','V_T_G',
       'T_F_D','A_D_L','N_F_P','N_J_C','T_P_J',
       'S_Y_Q','P_B_E','R_I_Q','X_V_D','Z_W_H',
       'W_O_R','F_B_X','W_L_V','U_M_Z','B_W_P',
       'W_D_V','K_D_J','H_F_Q','Z_B_V','O_K_G',
       'T_C_N','G_C_X','Y_S_R','T_N_P','H_P_X',
       'M_Q_Z','H_S_D','I_E_P','E_T_U','H_D_X',
       'K_Z_A','Y_M_F','I_K_Q','Q_Z_N','X_K_A',
       'I_A_V','T_H_U','T_Z_W','C_U_P','U_W_O',
       'O_N_F','C_J_Z','J_J_P','V_T_J','U_L_E',
       'Z_H_R','N_V_E','V_J_M','U_W_O','I_D_F',
       'K_Z_A','C_F_C','T_Y_D','F_Y_G','L_P_S',
       'F_T_E’,’C_J_Z','R_O_F','X_Y_I','R_Y_P',
       'M_I_B','N_O_X','F_G_O','U_F_Z','A_F_A',
       'U_T_F','Z_O_P','U_E_J','X_F_E','V_G_M',
       'L_E_H','U_M_H','F_Q_C','S_C_Z','Z_T_E',
       'X_H_W','W_M_T','L_O_C','V_P_M','Z_J_T',
       'T_B_X','L_P_Q','O_P_D','S_W_V','M_B_O',
       'M_Q_I','R_L_M','T_C_O','E_E_B','T_X_R',
       'L_Q_I','L_R_S','Z_R_U','P_A_Y','X_Q_X',
       'L_F_S','F_X_G','G_J_O','X_I_L','X_S_L',
       'G_F_Z','R_N_U','D_Z_F','T_O_F','N_K_R',
       'S_W_X','E_T_I','C_N_O','G_L_B','V_X_I',
       'P_N_O','R_J_M','D_I_B','M_T_K','R_G_L',
       'G_U_B','X_Q_Q','V_W_U','E_U_O','V_C_C',
       'T_R_P','V_S_P','D_N_G','O_T_N','E_W_H',
       'Q_G_C','S_P_S','R_A_B','E_N_T','W_X_H',
       'K_D_T','N_Q_R','U_T_G','H_D_S','V_P_M',
       'V_P_I','K_U_T','H_H_M','A_U_E','M_S_S',
       'A_W_T','L_H_C','J_K_B','H_I_N','C_X_V',
       'T_V_N','O_Q_K','W_W_H','R_C_W','D_H_H',
       'P_C_Y','T_C_O','I_A_V','U_R_P','E_L_F',
       'P_Y_O','E_N_N','D_X_P','Z_C_H','N_N_O',
       'N_O_C','G_K_K','Z_G_N','S_B_W','I_L_M',
       'R_X_J','X_C_H','K_T_C','F_G_U','E_X_D',
       'B_L_C','S_K_K','L_J_G','T_Z_T','U_I_L',
       'J_A_J','H_W_F','W_Q_L','E_X_D','G_E_S',
       'N_G_U','G_S_S','C_Y_F','I_I_S','Y_Y_I',
       'G_Z_F','F_H_L','U_R_C','E_V_J','T_W_P',
       'Y_Z_B','Q_Y_j','T_U_H','B_G_C','N_G_U',
       'L_S_T','N_X_Y','G_C_A','L_I_Y','G_M_L',
       'U_L_V','B_P_B','V_V_Q','F_G_G','F_V_A',
       'V_E_Q','C_S_L','E_C_J','V_N_G','R_N_R',
       'A_P_C','U_S_O','M_O_W','D_O_N','N_T_E',
       'G_B_Y','B_Z_Z','V_N_G','G_M_H','F_D_T',
       'J_N_A','Y_P_D','T_I_X','S_C_T','U_D_Y',
       'Y_Y_Z','B_W_V','W_K_J','D_D_E','E_D_C',
       'W_H_S','V_R_L','S_G_R','Z_D_H','H_W_Y',
       'X_G_X','T_O_B','Z_V_C','K_I_Q','P_C_Y',
       'A_M_I','M_D_S','A_P_H','K_Q_K','V_C_V',
       'F_R_W','B_M_D','R_D_B','X_L_H','R_I_K',
       'I_I_D','Y_F_U','G_K_J','N_J_G','K_F_C',
       'F_B_r','W_Y_A','N_W_N','V_X_L','S_B_C',
       'H_L_L','B_Q_L','Q_A_D','S_R_L','C_K_C',
       'Z_L_L','P_G_u','D_S_K','X_J_C','Q_N_Q',
       'C_K_C','P_G_P','S_R_L','E_W_C','W_R_M',
       'S_B_W','R_P_A','Y_C_P','D_M_D','V_U_L',
       'D_X_U','G_T_F','E_W_C','V_X_C','F_K_G',
       'T_Y_Q','K_X_O','D_M_D','A_W_U','L_Q_B',
       'C_M_W','V_X_C','F_K_G','D_T_D','G_Q_D',
       'I_T_u','T_X_V','R_C_W','W_C_G','Y_Y_R',
       'B_T_S','G_M_N','I_U_L','R_R_R','O_O_E',
       'P_J_P','S_U_N','V_A_I','U_M_R','W_Q_Y',
       'D_C_J','A_S_Y','L_G_O','X_I_X','X_H_Q',
       'V_K_V','C_T_E','D_I_L','C_Y_C','X_W_A',
       'K_P_F','I_U_L','E_G_E','Y_X_Q','G_K_G',
       'C_D_E','G_A_H','U_V_U','Z_P_X','T_K_J',
       'S_F_O','B_J_J','Y_X_E','H_W_E','X_K_I',
       'N_X_K','C_Z_W','G_Q_M','N_J_M','N_D_Y',
       'K_R_B','h_X_E','F_D_G','P_P_Z','B_C_Z',
       'X_K_E','P_F_T','Z_Y_Y','O_O_P','D_I_L',
       'U_W_P','C_L_I','P_P_Z','Q_Z_S','N_V_L',
       'L_T_Y','F_H_N','D_C_M','V_B_Z','X_D_G',
       'R_Z_T','X_A_P','H_H_B','F_X_I','H_B_Z',
       'O_B_R','O_W_W','V_B_Z','J_M_Z','S_R_Z',
       'E_L_S','E_R_L','B_M_V','P_F_A','D_K_O',
       'I_D_J','W_Q_L','W_M_H','Y_P_G','L_R_S',
       'W_X_Y','L_U_E','P_F_A','M_D_X','S_I_T',
       'T_V_N','G_F_R','P_W_E','G_Y_D','L_S_X',
       'Q_J_C','T_L_R','R_K_I','T_W_O','Q_J_C',
       'L_S_X','Q_N_Q','B_F_S','A_C_R','T_H_H',
       'W_P_u','J_K_D','O_D_Q','Q_X_C','V_B_Y',
       'T_W_C','J_V_D','D_N_B','B_Q_G','C_L_L',
       'J_K_D','E_I_R','G_P_K','X_C_Z','X_K_H',
       'D_Z_T','Q_R_I','F_O_M','W_E_N','N_F_I',
       'R_Q_R','K_V_U','J_M_O','E_W_E','P_H_A',
       'T_S_W','Y_Y_Y','D_Q_G','N_F_I','G_U_V',
       'C_C_R','K_U_I','L_D_G','B_J_Z','Z_W_W',
       'P_B_P','H_L_W','F_P_X','U_U_T','G_E_P',
       'Y_X_T','X_H_X','B_E_R','U_H_C','T_X_B',
       'O_r_G','S_R_A','C_K_O','N_O_S','O_Q_K',
       'X_A_F','R_Q_T','K_H_J','W_Z_H','W_Q_S',
       'C_F_I','S_G_E','T_V_R','O_X_B','L_H_S',
       'N_N_G','W_P_U','W_Z_H','L_O_T','A_C_K',
       'H_E_H','T_C_Y','Z_W_W','T_F_B','U_Y_H',
       'D_N_Q','W_N_G','L_I_T','H_Q_W','Q_H_J',
       'X_D_T','L_B_X','X_Y_W','D_C_C','M_A_R',
       'Z_Z_N','D_A_Y','R_Q_K','M_A_S','X_Z_P',
       'N_K_N','B_W_Y','R_B_T','V_N_T','V_G_M',
       'S_K_Q','U_T_I','G_G_Z','I_E_R','T_A_X',
       'W_S_Q','Y_Q_F','L_W_U','X_K_X','C_M_Y',
       'Y_L_E','B_S_l','J_L_I','A_R_C','o_A_D',
       'H_O_B','P_C_R','H_P_J','X_E_C','L_P_L',
       'W_O_A','N_P_L','I_E_O','S_G_U','L_O_N',
       'X_X_C','P_B_H','Q_J_I','Q_N_P','J_Q_U',
       'S_T_X','Q_O_S','E_J_O','U_C_O','Y_M_T',
       'B_W_Y','T_O_U','I_L_T','B_Y_Q','G_J_Y',
       'N_W_V','U_J_Y','Z_Z_S','L_V_O','Y_K_Y',
       'E_T_Q','H_T_F','P_I_G','D_M_J','N_D_Z',
       'N_K_D','O_P_D','Q_Q_R','L_W_C','K_K_J',
       'T_Z_M','F_W_N','N_H_V','W_Z_O','L_I_S',
       'G_N_M','S_T_P','C_L_T','V_P_I','J_C_I',
       'P_W_K','J_K_S','Q_X_G','E_P_H','U_B_T',
       'H_U_H','C_D_O','C_Y_F','U_F_S','X_Z_P',
       'P_D_P','K_Y_N','V_J_U','Z_Q_O','K_X_A',
       'G_M_L','Z_U_B','E_P_H','W_K_B','F_Q_Q',
       'G_I_I','C_X_A','Q_L_V','R_B_T','M_G_L',
       'X_Z_K','Q_J_W','Z_V_B','G_A_F','A_P_S',
       'A_U_G','Z_P_G','Q_K_I','B_D_O','O_Y_N',
       'P_U_M','R_A_P','I_Q_U','B_E_C','D_Y_W',
       'C_V_X','W_S_C','I_E_R','U_U_X','F_D_Y',
       'P_H_A','P_F_N','Z_X_L','L_G_O','E_U_R',
       'X_T_V','K_B_C','F_Y_X','U_I_O','D_Z_D',
       'I_O_J','D_A_Y','R_E_T','Q_G_O','C_Z_B',
       'L_S_I','C_K_P','Y_J_E','L_N_G','R_P_Q',
       'F_E_E','M_C_C','L_M_R','E_T_Q','Q_I_A',
       'Y_X_V','Z_G_N','X_B_G','O_A_A','Y_H_S',
       'R_P_U','L_T_E','X_N_V','L_J_M','G_O_S',
       'Z_A_E','Q_F_C','L_S_P','Q_H_P','I_Q_G',
       'Q_T_M','L_D_B','Z_N_Q','X_T_E','S_F_C',
       'V_W_I','U_L_Q','S_L_F','P_D_B','G_G_L',
       'S_F_C','Z_X_F','C_E_V','H_W_W','F_O_R',
       'K_F_O','A_C_C','C_O_L','A_Q_B','X_U_C',
       'I_X_Y','F_T_O','U_D_X','A_W_N','L_W_I',
       'X_L_I','N_C_U','K_G_S','F_A_K','Q_A_E',
       'U_I_F','I_O_U','I_D_F','I_J_W','A_M_O',
       'P_Z_Q','A_L_T','C_P_P','S_Y_X','T_R_F',
       'H_M_X','H_U_B','N_B_U','X_Q_I','W_P_Q',
       'N_W_K','F_I_T','J_Q_R','W_G_X','F_D_M',
       'U_R_C','O_L_D','W_Z_D','H_E_B','Z_M_U',
       'T_K_O','X_L_M','L_Q_Q','M_H_L','E_N_C',
       'S_C_n','L_P_U','B_M_D','k_K_K','L_T_I',
       'K_Z_L','F_L_N','E_T_O','X_E_I','Q_U_U',
       'K_G_S','H_O_Y','L_Z_R','P_D_F','S_O_O',
       'W_U_U','B_B_D','F_N_C','A_O_A','Z_P_C',
       'O_X_N','A_A_C','C_T_N','R_D_A','B_L_Y',
       'O_Q_O','X_I_T','L_Y_I','J_B_B','P_X_P',
       'S_O_E','F_F_V','A_Q_R','M_X_J','D_G_T',
       'O_H_H','F_O_F','K_W_L','R_Q_V','N_Q_U',
       'Y_S_N','U_O_O','S_O_X','X_D_B','Q_A_R',
       'T_P_I','F_O_P','V_C_R','l_J_G','N_H_Y',
       'D_R_D','A_W_N','T_W_Q','S_G_K','U_G_Y',
       'L_N_Q','I_I_X','B_G_I','W_J_S','Q_R_V',
       'Y_C_L','P_I_K','V_F_U','A_S_I','Q_O_F',
       'O_Z_A','I_R_J','R_U_M','D_C_J','U_Z_Y',
       'I_Y_I','I_X_Y','B_L_Y','P_F_D','Q_S_W',
       'S_Z_C','Q_S_F','Q_N_L','D_Y_D','S_E_A',
       'Q_B_M','M_Y_C','C_Z_A','Y_F_Q','G_B_X',
       'B_X_G','T_X_Z','V_Z_V','T_P_Z','F_O_U',
       'D_T_L','K_B_K','U_Z_A','V_H_N','Y_Z_O',
       'M_M_E','D_E_I','M_E_J','O_C_P','Q_Y_L',
       'M_L_T','W_I_Y','Y_D_G','I_Y_F','R_P_J',
       'U_V_M','N_O_H','N_I_T','I_T_S','X_E_L',
       'R_Z_E','Z_Q_E','S_D_M','U_Q_V','L_O_G',
       'Z_Y_L','U_A_U','U_H_B','P_F_K','A_M_G',
       'Y_Y_G','I_E_X','V_Y_Z','H_M_U','M_U_E',
       'H_O_B','F_D_Y','I_K_Z','Q_B_G','D_I_E',
       'Y_J_C','A_B_X','X_I_R','U_G_M','R_D_J',
       'K_P_E','Q_S_O','V_N_J','V_X_Y','N_N_F',
       'K_S_V','M_I_M','B_M_X','B_W_T','G_V_Y',
       'H_C_L','Z_N_P','F_P_C','G_F_I','Z_I_G',
       'U_C_Z','A_U_X','K_O_X','S_T_S','R_T_S',
       'F_D_O','Q_W_T','C_F_C','F_T_O','H_Y_S',
       'C_O_Z','O_U_J','R_C_X','B_X_N','P_Q_P',
       'T_U_G','O_N_F','D_P_G','R_W_R','W_I_R',
       'P_M_X','V_M_R','K_F_O','L_F_Z','B_R_M',
       'A_A_O','Z_X_C','Q_B_R','W_V_D','V_F_G',
       'Q_T_U','L_T_Y','W_N_Q','T_H_Y','B_C_W',
       'P_T_P','A_Y_Z','Q_T_Z','J_N_Q','X_J_l',
       'D_X_T','B_V_B','Z_F_U','B_I_G','H_N_W',
       'A_H_Z','U_R_P','P_J_U','S_O_B','K_R_A',
       'Y_N_C','U_G_Z','V_C_R','O_W_R','C_O_X',
       'X_N_B','C_J_G','S_U_M','P_M_G','V_L_V',
       'Q_Q_J','H_X_R','X_O_S','V_M_W','R_D_O',
       'N_X_H','R_Z_X','W_X_Y','I_X_M','D_N_U',
       'X_K_H','Z_O_D','V_J_Z','I_F_S','D_P_G',
       'V_V_P','E_V_S','X_C_I','O_Y_Y','K_N_H',
       'X_W_U','V_I_I','R_L_F','U_Y_W','F_F_X',
       'V_I_Q','N_H_W','T_N_Y','U_I_B','W_W_W',
       'V_R_P','U_U_P','Y_P_J','B_D_K','R_C_D',
       'Q_Q_R','W_V_E','T_K_E','D_P_B','N_J_G',
       'j_J_T','C_F_K','M_E_X','C_F_X','V_X_G',
       'H_M_L','A_O_L','C_S_U','T_N_J','N_L_T',
       'G_G_H','C_K_G','J_L_O','J_N_N','S_C_X',
       'S_R_K','D_U_C','Z_R_C','R_R_V','H_T_Q',
       'W_Y_E','C_Q_I','U_W_S','M_Z_W','X_V_D',
       'T_T_G','D_O_A','T_N_T','X_Q_D','Q_T_G',
       'Y_P_P','C_U_Q','K_V_C','S_Q_F','S_G_S',
       'G_C_Q','H_O_N','R_P_R','Z_O_O','Y_H_T',
       'S_K_H','T_U_G','H_W_I','O_E_O','H_O_L',
       'R_M_Y','P_D_E','B_H_G','K_E_E','D_N_M',
       'G_N_N','P_N_X','O_V_Q','Y_K_O','T_L_O',
       'Z_N_P','W_Y_A','D_D_T','Z_I_U','R_R_W',
       'M_T_X','H_E_G','X_Z_H','E_S_I','X_K_X',
       'U_Q_P','J_F_F','J_A_A','S_W_X','Q_l_9',
       'T_4_Y','K_M_E','F_8_W','Z_K_1','T_N_3',
       'Y_L_6','K_A_2','S_X_1','C_R_J','Y_6_S',
       'F_P_7','Q_I_9','R_Y_2','I_M_9','C_J_7',
       'T_P_4','Y_P_7','Q_K_9','C_J_7','J_I_2',
       'M_K_6','H_B_3','E_G_8','J_I_2','C_B_6',
       'A_D_6','L_O_8','O_Y_1','C_T_7','Y_O_4',
       'S_X_9','Y_E_5','U_C_7','U_T_3','N_P_6',
       'Q_I_9','B_W_9','Q_H_1','P_L_3','N_X_8',
       'E_G_8','I_J_4','Y_E_5','P_R_0','F_M_0',
       'Q_L_4','J_J_9','B_M_9','E_G_8','P_K_9',
       'U_T_3','G_V_5','R_A_4','R_Y_2','M_J_8',
       'F_D_5','Y_E_5','Q_K_9','M_K_6','X_D_4',
       'Y_P_1','Z_K_1','S_E_4','C_J_7','T_Z_7',
       'X_T_7','S_X_1','V_F_9','W_P_6','O_Y_1',
       'C_D_6','C_F_5','S_X_9','U_X_0','J_I_2',
       'J_J_3','X_W_4','I_M_9','X_U_4','T_J_8',
       'O_Y_1','Q_K_9','I_6_W','B_6_V','Y_4_N',
       'P_9_T','V_8_W','T_2_Y','J_9_N','A_7_C',
       'X_7_W','C_1_K','O_9_F','G_8_M','L_3_D',
       'P_3_M','W_5_F','N_7_G','P_1_R','U_8_Q',
       'K_9_P','P_8_P','T_9_L','C_2_N','C_2_N',
       'S_0_N','I_5_N','T_5_O','R_5_C','A_1_C',
       'L_4_Y','B_6_V','H_8_D','J_3_M','T_5_O',
       'T_6_S','T_5_O','V_5_C','P_9_H','G_5_L',
       'V_6_M','E_0_P','R_1_D','W_0_C','J_8_C',
       'V_4_E','N_7_G','Z_4_V','G_1_P','Q_8_P',
       'L_3_D','V_8_W','B_4_D','X_6_L','X_7_W',
       'R_6_R','H_0_Y','X_9_Y','A_1_N','F_0_I',
       'E_5_Q','F_3_E','O_3_K','F_0_L','C_0_S',
       'K_4_Y','B_0_X','B_8_B','D_5_H','B_0_E',
       'F_2_I','Q_5_T','Z_9_W','A_1_N','W_1_J',
       'B_0_S','W_8_H','E_J_Q','N_Y_V','H_H_A',
       'Z_L_P','U_H_B','F_C_T','Q_X_I','I_G_U',
       'S_X_X','C_F_Y','J_Y_K','Q_D_G','O_C_O',
       'V_T_G','D_U_U','Q_V_K','G_C_E','P_F_D',
       'W_B_G','X_B_K','A_F_T','W_W_L','T_J_Y',
       'Q_V_H','P_T_Z','U_X_O','F_U_V','G_M_F',
       'S_G_T','B_Q_L','X_H_F','F_O_M','P_N_X',
       'L_B_D','X_N_S','X_J_C','O_Z_T','I_F_M',
       'A_P_S','G_M_F','I_S_B','O_K_G','B_W_P',
       'N_P_B','I_P_S','G_U_J','U_D_B','W_L_N',
       'X_X_A','K_X_X','A_D_L','F_F_W','Y_P_U',
       'I_W_T','N_Y_B','K_M_E','B_I_X','W_O_R',
       'O_K_G','K_S_H','G_L_J','A_S_S','U_H_B',
       'F_L_G','A_A_C','W_D_V','F_O_F','B_J_O',
       'X_E_S','K_T_W','P_Y_Q','V_B_B','S_B_W',
       'T_C_N','T_P_J','H_U_I','W_I_R','U_H_B',
       'W_O_R','H_D_X','N_Y_B','B_I_O','E_K_W',
       'D_X_V','R_I_K','C_N_C','C_F_Y','A_E_G',
       'C_H_T','O_M_T','Y_W_J','A_A_C','B_X_J',
       'U_G_C','X_N_S','Y_S_R','E_Q_C','H_K_E',
       'B_X_Z','D_D_W','X_E_S','B_X_Z','B_D_L',
       'A_F_T','D_X_V','X_C_Z','I_G_T','I_W_T',
       'X_W_V','H_V_R','X_S_I','K_S_U','E_J_Q',
       'P_G_N','U_X_O','B_X_B','W_U_B','T_P_J',
       'D_S_O','R_G_C','Q_U_W','E_T_U','F_C_T',
       'K_Q_N','U_D_B','Q_A_U','D_J_X','R_I_Q',
       'B_V_N','Q_D_W','T_J_Y','W_D_V','B_X_C',
       'Y_W_J','T_P_V','T_D_T','D_S_O','I_F_M',
       'X_N_P','Q_U_W','Q_D_O','G_W_4','E_C_9',
       'I_A_6','V_Y_0','P_B_6','L_J_6','Q_E_4',
       'M_O_2','G_P_6','Z_I_8','W_R_0','B_F_4',
       'H_C_2','X_M_8','A_K_6','D_S_4','K_Z_1',
       'K_J_1','X_L_7','P_S_6','I_V_2','X_L_5',
       'E_X_2','T_A_1','P_K_1','F_T_8','R_R_9',
       'P_U_2','B_N_7','E_V_4','S_P_8','L_A_5',
       'W_R_8','C_W_1','X_L_7','W_C_1','X_L_7',
       'M_N_8','W_C_0','M_A_5','Z_M_5','D_F_2',
       'H_U_4','F_M_4','E_X_9','U_J_5','Q_X_2',
       'K_N_1','D_P_6','F_D_3','H_L_1','H_Q_9',
       'P_H_1','T_S_3','B_U_2','H_I_8','G_M_8',
       'T_A_7','Z_D_9','L_T_8','K_J_2','A_E_1',
       'R_U_8','L_A_2','A_H_2','Y_R_0','P_O_0',
       'U_T_8','X_W_1','N_Q_6','L_C_3','K_W_9',
       'G_F_1','E_E_7','G_N_6','C_N_3','M_V_5',
       'J_J_2','L_T_7','K_D_5','T_B_2','G_M_9',
       'V_V_6','Z_T_5','K_J_2','W_D_0','C_H_4',
       'F_K_0','I_C_7','G_X_1','I_V_3','O_D_5',
       'C_H_3','Y_T_1','R_J_0','R_W_9','A_Q_0',
       'I_U_0','K_T_0','C_N_3','J_U_9','K_Y_3',
       'Q_I_8','D_T_1','J_E_2','C_U_4','Q_Z_4',
       'K_I_9','K_S_4','P_T_7','V_C_3','O_D_3',
       'J_L_3','V_V_0','L_Y_7','A_M_6','X_S_0',
       'N_S_1','X_I_6','Z_G_0','W_C_4','K_S_4',
       'I_U_9','X_S_4','L_O_1','M_T_3','L_O_4',
       'E_R_3','Z_R_7','Z_D_9','T_D_6','M_J_8',
       'X_Y_1','C_H_7','K_P_5','I_E_0','C_L_2',
       'B_N_7','U_A_0','K_P_4','Z_B_9','X_F_8',
       'C_X_0','R_E_6','J_O_3','L_U_8','F_E_4',
       'Y_J_7','U_E_7','Y_E_7','Z_Z_1','Y_E_7',
       'N_R_8','I_U_6','S_P_5','W_O_2','M_P_4',
       'U_C_0','T_E_9','K_D_0','S_E_1','H_V_4',
       'D_D_5','X_D_1','B_K_3','J_W_5','N_A_5',
       'T_L_0','K_R_2','K_R_3','U_J_2','V_J_5',
       'W_B_5','Y_P_0','C_R_8','X_G_6','D_B_5',
       'I_L_3','E_E_0','L_H_4','L_Z_7','I_Z_8',
       'Q_O_0','M_J_1','S_A_5','L_T_9','P_X_3',
       'C_P_9','J_Q_9','J_C_2','A_I_8','Z_L_1',
       'V_W_5','F_C_4','P_T_3','G_A_0','I_X_4',
       'J_T_8','F_G_2','B_R_2','G_E_1','E_S_7',
       'B_I_7','U_S_5','T_N_7','O_N_7','I_Q_1',
       'B_L_4','P_T_7','K_P_2','A_K_4','B_U_1',
       'S_V_7','K_I_9','T_O_7','G_R_9','W_R_7',
       'A_U_4','J_Z_3','V_K_9','H_T_2','C_O_2',
       'D_Z_0','L_I_1','Y_Q_8','V_H_7','V_T_8',
       'T_W_0','X_B_2','P_T_3','A_G_4','N_A_6',
       'Z_V_8','L_L_9','H_T_1','A_S_7','Q_U_7',
       'D_S_2','W_M_3','T_L_7','E_R_4','K_Y_8',
       'G_A_8','V_T_8','L_I_1','Q_L_3','V_H_7',
       'Y_Q_8','R_Q_7','G_H_2','R_J_4','K_Q_1',
       'F_U_6','I_Q_1','N_Y_9','F_B_0','M_D_3',
       'N_W_8','P_S_3','O_D_2','I_W_5','L_W_5',
       'E_V_9','B_G_1','I_Q_5','T_E_9','Y_Y_7',
       'Y_E_6','D_L_3','Z_E_8','F_F_3','P_X_3',
       'N_W_0','C_D_6','R_J_4','M_I_8','J_J_2',
       'A_Y_0','U_G_3','D_B_8','F_X_6','Q_M_9',
       'T_C_4','T_K_8','C_N_6','S_E_2','Q_H_1',
       'Q_H_1','E_Y_6','N_F_0','O_J_0','D_R_9',
       'Y_U_6','B_T_4','T_W_6','I_I_0','M_G_1',
       'D_X_8','N_R_8','S_U_1','W_G_4','F_C_3',
       'K_S_1','V_J_4','C_U_8','V_B_4','I_U_6',
       'Q_B_7','X_Z_6','Y_S_3','K_Z_3','A_U_8',
       'F_H_1','C_J_2','R_M_5','A_H_0','L_P_5',
       'R_W_9','G_P_5','K_W_8','S_F_0','A_I_6',
       'J_G_4','M_U_1','Q_F_1','O_Y_1','P_N_9',
       'H_C_2','S_J_1','N_G_8','Z_O_2','G_L_9',
       'T_T_9','T_O_7','M_J_1','E_V_5','N_H_8',
       'L_Z_7','Z_Y_0','Y_S_5','M_J_1','B_H_0',
       'S_E_2','Q_X_2','Q_W_7','I_W_7','K_Z_3',
       'C_V_4','D_G_0','R_U_7','H_X_3','X_Z_2',
       'Y_O_1','E_L_9','J_S_8','Q_E_0','Z_L_9',
       'H_W_7','W_T_9','O_C_4','D_Q_0','O_T_9',
       'X_C_3','S_M_3','U_Z_7','N_C_6','I_Z_1',
       'S_R_7','K_M_2','L_W_5','X_O_9','I_N_3',
       'N_W_5','K_X_2','B_I_6','K_M_2','O_A_4',
       'T_I_8','K_D_2','G_G_8','Q_A_9','T_E_1',
       'W_W_1','A_X_7','Q_G_2','D_D_5','I_V_9',
       'M_A_0','S_I_9','B_X_7','R_M_9','O_O_9',
       'D_X_3','Z_J_9','D_C_7','G_U_2','K_D_3',
       'V_R_0','O_Q_8','T_C_9','P_D_1','G_C_3',
       'M_V_6','P_G_6','L_A_3','L_V_7','X_N_0',
       'N_S_0','Z_U_6','U_X_3','Z_B_8','S_N_2',
       'O_O_9','W_F_9','S_U_0','C_P_6','R_C_6',
       'I_G_3','X_G_7','I_S_8','K_Z_1','T_O_5',
       'R_L_0','H_Z_0','Z_Z_4','V_V_1','W_Z_8',
       'K_S_1','B_Y_8','T_T_1','Q_O_6','W_E_1',
       'I_Q_8','R_P_0','G_B_4','F_A_4','R_H_0',
       'D_V_1','V_X_1','K_J_8','Z_P_0','E_E_1',
       'M_F_5','S_X_3','S_N_8','A_H_3','N_N_9',
       'J_M_5','C_R_4','E_E_4','J_R_2','T_K_2',
       'E_C_3','T_F_0','U_C_6','V_E_2','S_I_9',
       'C_P_2','E_B_1','M_L_6','W_Y_9','J_F_2',
       'L_F_3','C_D_1','G_F_1','Q_A_9','I_Y_1',
       'K_L_0','D_N_8','T_E_5','F_T_6','N_V_8',
       'Z_Y_6','W_T_7','X_K_6','P_X_0','Z_D_4',
       'E_P_6','S_I_7','A_U_5','F_Y_0','K_S_1',
       'U_D_5','E_E_8','V_W_3','A_H_5','O_N_5',
       'X_X_6','U_D_6','H_F_9','W_T_5','D_M_5',
       'G_S_8','G_U_8','U_O_0','C_V_6','D_W_6',
       'A_Q_1','M_V_1','V_R_5','W_J_1','I_I_1',
       'K_N_1','F_H_9','U_A_1','H_Q_7','L_K_9',
       'Z_K_6','B_W_5','U_S_4','N_I_0','J_K_5',
       'I_R_7','H_B_3','J_I_4','P_N_1','K_E_2',
       'B_P_2','S_S_7','P_V_5','K_A_1','H_S_0',
       'D_D_0','W_M_5','S_S_7','G_Q_0','D_X_5',
       'D_F_3','R_V_4','T_B_5','T_L_4','X_D_3',
       'F_R_6','B_P_1','T_K_0','X_N_7','Q_Z_2',
       'Q_A_2','E_T_1','B_L_3','X_L_8','T_B_5',
       'I_I_1','F_V_5','W_A_5','O_Z_0','G_A_9',
       'Q_M_1','X_S_3','A_E_9','N_M_5','N_P_2',
       'E_T_7','J_O_7','O_J_5','F_Y_3','Q_G_2',
       'R_K_4','P_R_4','Q_O_1','F_C_1','U_O_9',
       'G_C_3','B_X_8','I_C_1','M_C_2','J_Z_0',
       'I_K_6','X_L_5','C_M_3','R_U_9','D_M_5',
       'Q_J_2','U_U_4','K_D_2','Z_L_9','K_Z_6',
       'S_H_3','L_Y_4','L_Z_0','Z_T_1','C_X_2',
       'V_U_1','V_R_4','Q_C_8','N_K_3','C_Y_5',
       'A_E_9','Z_E_9','O_E_6','S_Y_0','E_Y_0',
       'Y_F_2','F_X_5','H_P_1','O_L_5','R_Y_0',
       'T_K_6','X_Z_7','E_Q_1','C_A_4','U_D_4',
       'G_G_2','R_X_6','H_F_3','I_L_8','B_F_4',
       'Q_L_1','G_D_0','I_W_8','C_J_7','E_U_1',
       'G_P_3','W_H_2','H_D_9','U_T_6','J_T_6',
       'M_K_6','Q_K_4','Q_Y_7','M_Z_8','R_E_3',
       'T_B_7','V_L_8','T_P_6','F_O_7','A_E_0',
       'Z_H_0','G_W_9','G_G_0','S_Y_1','Y_K_6',
       'U_I_8','I_Y_7','A_U_3','Y_Y_9','H_S_3',
       'O_A_6','J_K_5','Z_Z_3','X_M_4','H_F_1',
       'K_S_1','U_K_2','L_U_9','Y_P_3','Q_T_5',
       'Q_F_2','M_B_4','D_F_2','S_W_3','B_P_2',
       'N_B_1','E_H_2','S_X_4','R_K_3','Z_X_3',
       'G_L_8','V_I_6','D_W_7','T_D_5','A_D_9',
       'X_L_3','M_N_3','L_O_6','A_M_1','O_T_1',
       'J_Y_6','Y_L_0','V_B_9','R_5_M','D_T_P',
       'D_V_9','H_U_2','X_R_6','U_U_U','N_N_N',
       'E_H_8','O_O_1','S_U_4','Z_F_3','E_G_4',
       'E_H_8','O_O_1','S_U_4','Z_F_3','E_G_4',
       'Z_G_3','T_R_2','J_C_1','B_L_0','H_J_5',
       'G_Q_7','K_A_3','R_W_7','N_O_2','J_M_0',
       'E_W_5','O_Z_3','L_I_5','C_V_0','U_Z_9',
       'K_X_1','I_P_5','E_X_1','Q_X_6','Y_C_0',
       'B_U_8','Y_Z_0','H_W_8','O_G_8','Q_P_0',
       'R_H_6','H_Z_2','Z_Z_5','D_O_9','P_O_8',
       'R_T_6','B_X_9','J_U_2','Q_C_5','O_K_1',
       'B_Q_1','C_Q_9','Z_A_4','D_Z_7','Q_N_9',
       'U_U_9','N_K_2','N_Q_2','R_P_8','R_G_5',
       'O_X_1','V_K_8','G_V_2','C_Z_5','K_H_6',
       'O_Z_5','C_Y_7','L_I_2','I_I_3','B_M_0',
       'T_I_1','B_O_6','X_X_8','T_V_9','U_B_0',
       'F_F_5','C_E_0','C_A_7','Z_H_2','A_A_6',
       'X_S_5','U_V_7','I_U_4','N_X_0','V_T_2',
       'W_W_6','H_N_4','Y_Z_0','F_X_7','D_X_1',
       'O_B_2','V_V_5','S_Z_7','M_E_5','G_J_5',
       'Y_V_8','S_B_1','H_Y_4','Y_C_4','U_T_0',
       'N_O_7','Q_X_1','G_T_0','Q_B_5','A_I_7',
       'E_J_1','G_U_7','C_E_2','G_K_5','S_F_2',
       'B_O_5','Q_F_0','N_V_1','I_G_5','O_B_7',
       'D_Q_6','H_M_3','N_X_4','B_U_7','N_K_0',
       'Y_Y_4','Y_C_1','A_A_9','L_W_0','L_Q_2',
       'D_M_2','K_T_2','S_N_6','U_Y_7','E_X_0',
       'L_X_7','X_H_6','Z_N_3','W_I_9','U_Z_5',
       'R_T_1','B_N_6','U_V_2','G_X_7','Z_Y_7',
       'O_Y_8','X_F_5','V_Z_3','J_Z_2','V_O_3',
       'R_Z_7','S_Z_7','W_F_4','J_V_0','E_R_8',
       'D_G_5','Z_X_8','L_A_9','B_F_5','K_W_6',
       'N_K_6','C_I_9','H_O_0','D_H_3','K_X_4',
       'G_Q_6','T_D_0','E_D_3','D_U_0','P_D_4',
       'P_C_2','Z_U_3','X_Z_8','J_N_5','G_L_0',
       'I_G_7','P_M_2','T_A_9','D_Q_7','K_K_5',
       'T_T_4','Y_G_4','S_D_6','Y_Z_0','S_O_7',
       'P_S_4','H_Y_2','Y_Q_1','P_W_0','C_H_2',
       'C_L_5','Z_R_6','L_T_6','F_E_3','Y_X_5',
       'I_C_3','K_C_8','I_B_0','V_G_7','G_I_8',
       'U_V_6','I_O_6','G_S_5','W_R_1','E_E_9',
       'V_U_7','A_X_6','P_Q_8','D_S_0','K_N_2',
       'V_D_3','S_R_9','E_K_3','S_L_6','F_Q_8',
       'T_D_3','J_I_7','M_K_4','T_L_1','J_G_6',
       'G_J_3','T_C_7','O_R_3','I_W_4','I_H_2',
       'X_W_5','T_W_8','E_J_1','O_Q_2','Q_B_5',
       'B_O_1','J_T_7','P_T_8','I_H_1','B_B_6',
       'Z_G_6','U_Y_0','K_E_5','X_A_8','D_K_8',
       'R_R_4','M_F_1','G_I_4','D_F_8','Q_H_8',
       'Y_L_3','I_N_7','P_F_1','R_E_5','Q_N_1',
       'I_O_7','G_S_7','J_K_2','U_Z_3','G_D_6',
       'K_L_5','B_K_5','P_U_0','F_N_6','J_Z_7',
       'R_W_3','N_P_3','Q_H_3','W_C_7','I_T_1',
       'E_U_5','I_H_1','L_B_6','K_E_6','V_I_7',
       'L_G_0','S_W_2','G_Y_1','K_C_2','J_B_0',
       'X_Q_3','X_F_9','X_X_8','Y_U_0','N_U_9',
       'C_O_5','W_E_0','H_X_6','N_E_5','F_O_8',
       'W_I_0','H_E_3','U_R_0','S_A_8','I_Z_5',
       'T_P_8','I_I_8','N_C_4','F_X_3','B_H_4',
       'N_N_5','Q_O_9','J_T_3','T_S_5','B_J_7',
       'O_K_8','L_L_0','B_H_5','C_C_5','Y_C_4',
       'T_J_1','F_D_7','D_J_3','H_X_5','T_L_5',
       'O_R_5','X_U_3','W_J_7','T_U_9','K_Q_5',
       'J_G_9','Z_Q_4','C_K_0','F_I_8','E_P_2',
       'X_N_2','X_A_8','Y_Y_4','R_Z_4','V_W_6',
       'J_E_7','Q_L_0','P_L_7','V_L_6','L_X_0',
       'W_M_0','S_S_6','M_H_4','T_U_3','X_W_5'
       'S_A_8','Z_B_2','R_Q_5','M_M_9','I_N_5',
       'Q_C_7','B_F_6','X_V_2','R_P_2','X_W_7',
       'G_T_8','I_L_1','Q_F_0','S_P_5','A_R_1',
       'Q_R_9','D_F_5','D_M_3','I_C_2','Z_X_9',
       'Z_Y_4','G_A_6','W_R_3','X_K_2','M_Z_1',
       'L_R_1','E_E_5','W_I_6','B_O_6','S_C_2',
       'W_W_7','Y_Y_2','C_B_8','X_L_6','Z_O_3',
       'G_A_5','K_U_0','F_Y_4','F_H_3','X_M_9',
       'U_H_3','D_W_5','P_T_6','W_J_0','O_Q_9',
       'J_X_5','X_E_3','F_T_0','Y_F_1','W_A_1',
       'F_R_5','T_S_7','H_C_6','I_K_3','W_E_8',
       'V_U_0','O_C_9','R_I_8','B_E_2','E_U_8',
       'G_K_9','V_O_0','C_B_9','P_D_3','O_L_0',
       'B_N_9','G_Y_1','M_U_0','M_S_0','T_L_5',
       'E_G_4','E_U_7','C_N_4','T_R_7','O_T_0',
       'X_G_8','Y_I_0','D_N_0','Z_F_3','K_U_1',
       'A_R_1','O_B_7','K_W_1','G_Q_3','K_C_8',
       'I_K_3','P_W_0','L_O_5','F_O_2','P_Q_9',
       'K_H_4','L_P_3','C_N_5','Q_D_5','N_H_5',
       'U_Z_1','J_V_4','R_X_2','B_M_0','Y_Z_3',
       'B_Z_4','O_Z_5','G_F_2','B_W_2','C_M_0',
       'A_Z_0','S_D_2','Y_E_4','T_I_6','X_W_5',
       'D_Y_1','N_R_6','K_V_3','F_S_8','T_S_5',
       'E_O_6','H_D_2','T_S_0','X_V_2','C_Z_9',
       'Z_N_9','O_B_0','L_O_2','R_B_4','U_X_4',
       'Y_X_8','E_J_1','P_T_6','P_E_5','X_N_6',
       'E_T_9','V_W_0','Q_M_2','I_G_2','X_N_4',
       'M_W_9','W_W_4','Q_I_3','O_Q_1','H_F_2',
       'S_C_3','N_R_6','W_J_6','Z_Y_8','C_F_0',
       'R_E_2','K_F_1','V_T_3','L_I_5','W_A_1',
       'E_K_5','B_A_8','P_E_4','H_D_3','M_S_0',
       'N_R_5','I_Y_3','P_V_6','I_X_5','J_J_7',
       'D_G_2','I_O_5','K_X_3','T_W_8','L_U_3',
       'C_O_6','N_W_2','L_W_4','E_A_9','T_G_2',
       'O_O_0','I_G_5','E_F_2','T_S_7','F_X_9',
       'H_D_2','X_V_2','C_Z_9','Z_N_9','O_B_0',
       'L_O_2','R_B_4','U_X_4','Y_X_8','E_J_1',
       'P_T_6','P_E_5','X_N_6','E_T_9','V_W_0',
       'Q_M_2','I_G_2','X_N_4','M_W_9','W_W_4',
       'Q_I_3','O_Q_1','H_F_2','S_C_3','N_R_6',
       'W_J_6','Z_Y_8','C_F_0','R_E_2','K_F_1',
       'V_T_3','L_I_5','W_A_1','E_K_5','B_A_8',
       'P_E_4','H_D_3','M_S_0','N_R_5','I_Y_3',
       'P_V_6','I_X_5','J_J_7','D_G_2','I_O_5',
       'K_X_3','T_W_8','L_U_3','C_O_6','N_W_2',
       'L_W_4','E_A_9','T_G_2','O_O_0','I_G_5',
       'E_F_2','T_S_7','F_X_9','T_O_4','V_C_9',
       'S_K_1','K_C_0','D_D_2','F_O_0','J_L_8',
       'B_U_6','J_F_4','E_L_4','P_A_9','R_R_5',
       'F_X_9','T_O_4','V_C_9','S_K_1','K_C_0',
       'D_D_2','F_O_0','J_L_8','B_U_6','J_F_4',
       'E_L_4','P_A_9','R_R_5','W_V_3','J_L_1',
       'M_D_5','X_Y_2','V_V_4','T_R_1','E_E_3',
       'Q_X_7','S_P_4','Q_C_1','P_X_6','G_I_3',
       'W_U_9','X_I_4','T_P_0','N_L_4','I_D_2',
       'T_C_4','M_H_0','A_Z_7','M_U_9','X_J_5',
       'T_V_4','K_O_7','K_V_3','F_F_8','Z_X_5',
       'J_Z_2','I_G_8','H_O_0','R_K_2','Q_E_5',
       'F_M_5','B_F_5','Y_I_0','H_P_4','O_C_0',
       'N_K_2','N_Z_7','Z_W_4','Q_Z_5','B_D_6',
       'X_I_3','K_F_9','Y_Z_0','G_V_4','U_I_6',
       'G_G_5','D_Z_5','J_H_9','U_H_3','O_R_5',
       'I_H_0','I_F_0','C_C_4','A_X_0','U_Z_2',
       'T_L_5','W_E_9','Y_X_1','Z_Y_2','K_G_6',
       'E_P_9','X_S_5','W_Q_2','U_D_9','L_L_2',
       'F_I_2','P_E_4','K_C_9','S_A_4','I_X_2',
       'Y_R_6','Z_W_6','Y_Y_5','Q_Q_6','X_B_8',
       'T_N_6','Q_V_0','B_U_9','V_R_6','Q_B_4',
       'R_T_0','H_O_7','V_L_6','Y_P_6','C_N_2',
       'K_F_5','F_J_2','J_G_6','J_X_5','U_U_7',
       'M_L_7','J_L_6','F_W_0','R_J_1','K_N_6',
       'K_S_3','D_Y_9','Y_P_2','I_O_7','G_T_1',
       'C_I_7','D_H_3','O_C_6','G_Q_7','B_Z_4',
       'D_B_0','O_F_8','L_K_0','E_V_2','C_S_4',
       'A_O_5','W_W_2','F_S_8','H_D_1','I_O_5',
       'A_X_0','N_Z_7','G_Q_1','V_R_9','G_A_6',
       'S_B_0','G_J_4','J_F_1','F_H_3','I_T_3',
       'w_5_f','p_2_c','w_7_k','u_2_c','f_6_q',
'g_8_i','k_3_6','l_8_g','n_1_t','x_0_u',
'z_6_o','s_3_1','t_4_b','a_6_8','r_7_f',
'h_2_j','a_1_c','r_0_d','g_8_m','o_4_l',
'y_2_g','x_0_u','p_9_w','n_1_2','q_6_s',
'q_4_0','g_5_l','y_6_3','q_0_w','j_4_3',
'x_5_e','f_9_o','p_8_4','k_5_c','w_1_k',
'g_3_9','y_0_0','y_0_o','k_2_6','c_4_i',
'c_7_m','m_2_e','w_3_a','u_6_f','q_0_w',
'v_1_w','k_2_e','g_9_n','x_7_0','r_6_r',
'y_8_e','w_3_a','q_4_0','n_8_x','b_0_v',
'm_8_c','u_0_u','v_6_v','g_9_4','v_0_i',
'n_9_i','k_0_r','s_9_n','w_5_s','u_1_p',
'd_5_4','r_1_b','i_5_0','e_2_r','g_8_8',
's_2_t','d_7_2','k_2_k','y_0_2','w_4_g',
'i_6_w','o_9_t','y_4_n','k_2_6','t_1_l',
'p_4_x','q_6_u','b_2_o','t_4_u','d_0_6',
'x_5_t','y_5_k','a_2_z','c_0_o','k_4_h',
'k_9_y','z_8_1','l_1_y','p_4_2','k_0_e',
'z_8_1','e_5_o','b_2_j','d_0_6','s_5_e',
'b_0_s','s_6_r','o_1_3','t_1_q','y_4_n',
'd_8_s','y_0_6','y_1_w','i_3_n','f_0_i',
'h_7_8','b_7_q','o_1_3','u_2_c','m_6_u',
'o_9_l','z_2_g','k_4_w','t_3_4','u_6_e',
'u_4_7','g_4_y','w_4_a','e_8_g','l_2_p',
'g_0_d','s_8_l','j_9_a','s_1_1','t_9_e',
'm_6_4','n_4_0','v_3_4','f_8_m','r_5_x',
'p_3_n','t_1_q','k_1_q','t_9_e','d_0_v',
'x_6_r','t_2_3','n_9_p','d_4_k','i_8_j',
'e_5_t','p_5_p','i_6_w','i_5_0','o_6_9',
'j_9_1','v_4_m','w_1_h','t_9_5','z_6_4',
'f_3_i','e_2_h','e_3_y','c_2_z','j_2_r',
'j_2_h','f_3_i','q_4_0','k_6_g','k_3_r',
'i_6_2','v_6_6','n_3_8','a_2_v','e_1_v',
'j_9_r','s_4_j','m_6_v','c_4_g','f_3_d',
'g_8_8','s_4_c','s_3_1','k_5_a','d_4_k',
'n_1_8','i_4_x','w_3_d','v_7_7','l_3_k',
'd_8_v','b_2_d','g_0_z','g_8_c','w_7_8',
't_2_f','t_0_7','t_0_k','z_5_7','s_0_z',
'e_1_4','x_8_5','n_0_p','b_2_5','b_2_b',
'k_7_d','s_9_m','m_7_2','t_8_z','b_3_z',
'p_1_g','f_5_j','e_8_3','w_8_1','a_8_4',
'o_8_m','n_0_p','q_4_0','e_3_9','j_4_3',
'f_3_8','p_4_q','o_7_m','s_9_m','e_0_q',
't_4_2','e_3_b','u_6_y','g_9_4','k_0_e',
'o_9_l','v_6_x','n_5_j','z_7_0','l_7_r',
'b_5_1','j_3_m','f_3_y','g_6_x','q_0_i',
'w_4_o','b_4_s','q_2_y','k_2_6','a_8_z',
'd_8_s','b_8_s','w_1_j','f_3_e','w_3_a',
'i_3_t','y_7_r','u_2_a','b_9_f','v_2_4',
's_7_2','b_5_1','t_0_7','k_9_o','f_1_m',
'n_4_3','r_4_p','o_2_3','g_9_4','p_6_s',
'g_8_t','h_1_j','g_8_s','u_8_o','q_1_2',
'f_3_o','z_7_y','q_3_h','e_5_t','b_2_y',
't_0_s','c_4_g','h_5_g','c_8_5','t_3_4',
'e_3_1','w_4_3','t_4_3','t_4_b','h_7_8',
'm_2_p','b_5_2','b_7_n','o_6_b','t_4_b',
'k_0_e','d_7_t','r_7_i','f_8_m','l_4_6',
'x_7_0','c_8_0','g_1_e','v_3_2','i_3_i',
'g_9_k','o_8_s','j_4_3','p_4_o','s_6_r',
'm_7_x','d_7_t','m_9_q','e_1_8','r_9_n',
'q_9_t','d_3_7','g_2_3','b_4_s','o_3_h',
'f_9_m','c_3_7','u_6_f','m_2_p','a_8_l',
'x_9_y','o_8_m','t_1_l','b_5_1','c_6_r',
'f_1_s','y_0_0','e_8_k','n_8_x','g_4_w',
'o_4_p','y_8_r','c_4_g','c_6_f','t_1_4',
'h_2_j','t_5_y','z_5_n','w_0_c','p_9_q',
'n_6_8','k_3_6','m_2_0','d_1_1','f_9_o',
'p_0_s','q_9_s','u_2_y','s_1_1','f_3_y',
'c_2_1','t_2_6','k_4_w','t_2_3','m_7_3',
'r_7_f','v_8_g','u_3_n','m_2_l','p_2_b',
'p_3_n','q_2_y','d_6_w','f_8_m','k_5_c',
'y_8_j','i_3_i','e_8_g','s_9_n','l_6_k',
'u_6_y','l_7_r','e_3_1','t_5_y','u_3_3',
'b_0_v','x_7_l','j_2_p','z_2_u','j_8_q',
'r_8_8','z_6_r','j_0_0','i_7_8','f_9_d',
'x_8_u','r_9_e','v_4_o','i_1_i','i_6_e',
'l_5_p','z_5_o','r_6_z','t_9_o','q_5_u',
'u_1_o','s_0_v','b_0_1','s_9_s','c_8_f',
'z_8_n','w_1_5','m_2_y','y_1_k','e_6_4',
'u_0_s','i_3_7','f_8_h','i_4_7','m_0_l',
'f_5_e','f_7_e','d_7_b','j_6_n','d_0_4',
'r_4_p','s_1_p','l_6_o','i_5_3','z_7_g',
's_0_8','w_7_c','e_5_d','s_6_6','a_7_o',
'c_4_p','a_7_f','y_7_b','f_5_6','y_5_4',
'l_5_o','e_6_a','o_0_w','c_6_b','b_6_6',
'v_7_m','j_0_i','s_0_0','j_6_0','k_9_t',
'y_3_1','q_0_p','b_9_k','l_5_7','x_5_a',
'p_2_h','q_4_m','m_8_3','p_8_k','b_9_1',
'r_0_7','k_2_b','w_5_v','s_3_2','w_4_h',
'c_3_4','b_5_p','p_8_q','l_9_f','s_2_o',
'i_5_k','s_2_e','g_6_f','s_0_s','s_2_3',
'q_1_x','d_1_n','e_4_m','s_6_q','k_0_c',
'l_0_l','x_4_h','l_7_k','e_9_9','w_6_3',
't_8_3','m_4_a','q_4_z','b_2_r','l_9_h',
's_1_8','f_6_7','u_0_3','s_8_1','y_2_h',
'x_5_5','s_2_d','b_1_g','c_0_3','t_7_c',
'l_3_4','b_0_n','i_0_g','b_0_y','l_4_p',
'x_6_e','y_7_a','n_4_w','p_5_m','e_7_3',
'v_1_c','g_2_2','x_1_y','y_3_7','s_1_e',
'q_2_2','n_1_3','e_8_x','g_3_g','p_9_m',
'x_4_0','p_0_u','f_8_q','d_0_k','e_3_v',
't_7_a','d_7_y','b_3_x','q_1_1','f_9_s',
'z_7_q','j_8_n','x_7_x','p_1_w','s_7_9',
'v_7_b','i_4_9','m_7_f','j_5_y','s_6_x',
'w_0_o','s_7_7','p_0_u','u_9_1','c_3_6',
'z_4_s','l_4_e','x_3_d','f_7_7','d_1_e',
'k_9_1','s_0_t','s_7_p','s_2_o','i_3_a',
's_9_h','h_1_r','c_1_x','x_5_3','z_4_v',
'w_5_i','g_8_k','y_6_y','g_0_c','m_1_b',
's_2_r','s_9_4','n_3_n','s_2_r','n_9_w',
'e_9_8','i_4_9','b_8_x','j_7_8','x_9_x',
's_7_q','x_5_c','j_0_7','c_6_w','i_3_w',
'p_2_q','o_5_9','s_0_u','y_6_p','c_0_t',
'u_0_m','h_6_5','s_1_h','w_9_l','x_8_4',
'p_9_u','r_2_y','r_2_h','j_4_5','x_1_k',
'r_7_u','p_9_i','i_7_x','w_1_s','q_8_q',
'o_3_c','e_2_b','t_2_h','h_6_f','z_2_s',
'g_3_g','x_7_1','l_1_c','x_7_b','l_5_n',
'g_8_g','q_1_q','f_1_0','u_9_2','i_5_9',
't_1_u','s_9_s','s_3_k','j_4_0','x_8_o',
'm_9_p','j_6_6','y_4_t','f_7_c','o_1_c',
'w_9_y','p_1_p','d_4_b','l_0_i','u_8_1',
'y_4_h','x_8_8','i_8_r','i_3_7','r_5_s',
'u_4_z','t_1_u','q_3_c','x_0_s','m_7_8',
'z_3_b','g_1_l','m_1_8','x_0_n','d_3_5',
'r_7_6','l_0_0','x_7_b','w_6_8','h_1_g',
'j_4_j','d_1_t','q_3_n','q_3_1','f_6_e',
'd_0_4','h_5_h','d_2_7','q_0_k','c_4_r',
'j_6_l','s_0_f','c_2_q','r_6_o','r_4_4',
'n_8_4','n_2_w','y_4_t','m_1_p','v_7_9',
'i_1_i','g_1_c','y_3_h','z_4_6','s_4_1',
'f_6_f','j_9_4','c_1_e','v_5_c','i_6_h',
'z_6_h','q_5_j','r_7_3','m_0_b','e_8_u',
'z_2_c','x_0_s','d_1_n','w_7_1','j_7_l',
's_1_e','x_3_2','z_8_q','a_7_l','x_3_x',
'p_4_3','u_0_1','v_7_s','i_2_q','y_7_9',
'o_4_c','t_6_t','n_4_s','d_8_h','a_1_n',
'b_3_d','f_2_f','j_4_d','h_8_8','m_5_g',
's_8_0','k_9_h','n_7_0','j_0_k','d_4_3',
'o_0_e','y_2_w','j_3_a','w_7_y','h_h_h',
'v_6_9','x_3_2','q_0_c','h_7_3','f_9_r',
'z_4_v','k_7_v','c_0_m','i_4_9','e_7_u',
'a_2_9','y_0_s','s_2_m','g_9_5','p_2_0',
'v_2_t','p_2_d','s_2_a','q_2_0','n_6_k',
'g_0_h','b_8_6','y_3_5','m_3_u','d_3_4',
'r_8_1','m_1_p','j_2_j','y_3_i','t_8_i',
'x_3_m','c_3_s','j_2_w','d_0_2','b_1_5',
'u_6_n','z_6_j','u_1_5','t_1_k','e_4_n',
'x_9_p','m_4_l','i_2_1','o_4_g','i_4_5',
'n_6_3','s_3_r','s_6_c','k_1_6','i_4_h',
'f_4_f','i_4_h','x_8_l','u_3_1','l_3_2',
'p_3_h','j_4_g','q_2_z','h_2_2','j_6_n',
'w_6_5','l_0_1','m_1_p','f_6_p','l_6_o',
'c_9_9','h_3_l','l_1_u','r_5_k','p_9_p',
'q_4_u','h_6_v','o_6_e','z_3_d','y_1_r',
'f_8_2','i_8_e','e_6_1','b_3_i','n_4_n',
'k_6_a','m_0_k','x_8_o','p_9_k','e_8_q',
'r_9_p','f_8_w','h_6_v','k_3_r','k_0_n',
't_3_w','s_9_6','h_3_3','s_7_q','z_8_w',
'u_7_3','e_2_a','p_7_9','r_8_s','w_6_0',
'd_3_i','r_2_4','w_6_6','i_5_1','q_8_8',
'p_8_m','j_0_o','x_5_3','a_9_8','n_7_g',
'g_4_v','x_1_n','d_8_3','w_3_o','p_0_6',
's_1_e','c_0_9','q_4_p','y_0_x','f_8_h',
's_0_2','e_6_t','l_7_4','z_4_s','r_8_d',
'd_0_t','q_1_z','r_2_k','v_1_6','l_2_8',
'w_4_w','u_1_g','b_9_2','s_0_s','u_7_v',
'c_0_9','r_8_q','o_6_s','n_8_q','l_6_r',
's_7_6','p_7_z','k_7_0','o_2_1','j_0_i',
'u_3_1','q_2_3','y_9_a','v_6_r','a_9_a',
'p_2_d','h_8_5','b_6_v','a_8_q','w_6_0',
'd_1_4','c_7_5','u_2_9','r_9_5','x_5_4',
'f_3_s','o_9_n','b_8_x','c_5_v','o_2_c',
'x_0_5','j_4_0','r_5_q','s_3_y','j_5_y',
'n_9_y','r_9_e','s_6_e','l_7_z','w_5_v',
'g_0_0','e_9_a','s_2_r','r_6_9','i_8_r',
'x_3_s','o_3_r','h_4_9','r_0_f','q_1_u',
'b_7_a','n_8_k','r_3_z','e_7_9','r_6_w',
'p_5_w','y_8_8','m_2_j','l_9_b','x_5_o',
'k_6_r','l_1_e','y_5_x','i_1_p','b_9_i',
'r_0_g','d_6_n','z_4_v','f_1_j','b_5_d',
'd_4_1','m_8_0','o_4_h','x_4_m','x_2_6',
'i_2_1','x_1_q','b_0_x','e_6_4','g_8_u',
'j_6_9','r_8_s','d_8_d','o_6_l','y_8_u',
'h_4_2','q_4_i','q_4_q','h_2_u','j_3_u',
'z_1_6','e_6_7','n_1_x','q_5_j','q_8_q',
'q_4_p','q_4_p','b_9_p','y_0_1','o_7_n',
'z_1_0','v_6_c','y_6_c','n_0_l','c_3_0',
'n_0_g','n_0_7','z_4_4','u_7_x','a_4_a',
'j_4_v','n_8_z','w_5_x','g_1_p','f_2_5',
'd_5_5','m_7_a','d_1_5','c_7_g','h_5_6',
'i_4_9','r_5_e','g_2_i','s_9_d','e_8_q',
'd_4_7','u_1_u','q_9_z','x_4_x','j_7_f',
'd_9_t','r_9_k','z_1_7','l_3_x','m_6_i',
'i_6_u','z_5_p','f_0_0','g_0_9','a_9_q',
's_1_h','v_3_k','g_4_9','a_2_1','n_9_6',
'l_0_j','q_4_1','g_8_n','w_1_f','a_6_g',
'g_7_g','d_8_h','e_3_8','w_4_w','f_3_x',
'q_6_c','i_0_e','w_2_d','f_3_z','a_0_6',
'v_8_b','v_8_x','s_8_s','x_6_s','b_9_j',
'u_0_n','z_1_m','u_0_n','i_7_f','k_5_m',
'm_2_y','x_5_u','d_9_2','w_9_l','x_7_y',
'g_4_o','t_3_q','h_3_z','d_9_b','u_7_v',
's_3_e','a_3_9','v_1_d','c_2_q','b_7_m',
'y_6_s','a_0_p','i_5_a','a_6_7','j_7_l',
'v_7_8','l_9_y','y_4_3','t_1_w','m_0_s',
'x_1_v','m_0_k','l_4_t','h_6_m','r_0_x',
'p_6_6','p_6_9','z_3_b','x_6_o','j_1_z',
'l_9_7','o_0_k','q_2_b','f_6_9','i_4_a',
'i_7_1','c_0_5','c_4_d','l_9_t','q_9_1',
'i_0_e','i_5_e','f_8_h','y_4_e','z_3_g',
'b_8_c','z_3_b','j_5_j','p_0_7','i_5_1',
'c_6_n','e_7_i','u_8_d','e_5_i','g_1_g',
'r_0_5','p_2_4','m_1_t','a_8_b','g_9_y',
'e_0_8','w_4_b','j_1_3','e_5_5','r_2_u',
's_8_3','y_0_b','w_3_3','n_7_q','r_2_w',
'x_3_u','w_3_g','g_1_q','x_5_z','g_0_w',
'f_6_5','p_7_p','a_5_s','c_3_s','b_3_9',
'n_2_s','d_9_d','w_3_u','h_9_i','t_2_y',
'z_3_m','s_0_4','q_1_a','h_4_4','s_9_4',
's_9_h','x_5_o','r_0_0','s_0_e','o_4_m',
'i_3_f','h_1_0','m_2_p','o_2_z','l_8_o',
'h_1_2','q_5_t','w_1_6','o_8_0','m_3_9',
'b_0_9','s_7_s','p_0_3','t_5_1','o_6_0',
'g_0_w','t_2_n','o_4_a','s_6_h','r_5_s',
'm_6_5','d_6_r','c_9_8','e_4_x','l_7_6',
'c_5_o','m_5_0','p_1_w','v_1_5','p_3_p',
's_1_9','o_8_1','b_9_w','b_2_u','z_1_c',
'w_6_6','i_4_t','t_2_m','u_9_3','s_6_x',
'p_3_9','v_8_f','k_1_k','s_6_q','h_8_5',
'f_6_e','v_7_k','t_6_t','i_6_v','y_0_1',
'd_1_2','z_6_x','q_4_3','b_3_2','w_7_c',
'o_3_5','e_3_8','z_4_4','t_8_t','y_0_j',
'e_4_x','u_7_q','g_7_7','v_9_u','r_4_3',
'c_4_1','l_1_z','s_9_u','r_0_h','v_4_8',
'n_9_e','l_3_3','a_9_c','w_6_w','n_0_b',
'x_6_t','m_5_l','l_5_n','d_9_q','m_8_o',
'z_3_b','j_0_8','x_2_c','s_7_i','g_4_1',
'r_6_z','e_7_9','s_1_8',]
@bot.message_handler(commands=["start"])
def start(message):
	f = message.from_user.id
	if f == SUDO:
		mas = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(يوزرات ثلاثيه)", callback_data="SS")	
		G = types.InlineKeyboardButton(text ="(يوزرات بوتات)", callback_data="F8")
		V = types.InlineKeyboardButton(text ="(يوزرات مميزه)", callback_data="F100")
		M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
		mas.add(G,K)
		mas.add(V)
		mas.add(M)
		bot.send_message(message.chat.id, text=f"- أهلاً {message.from_user.first_name}  !\n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
	else:
		rr = types.InlineKeyboardMarkup(row_width=2)
		me = types.InlineKeyboardButton(text="مجهول",url="https://t.me/k_8_u")
		he = types.InlineKeyboardButton(text="حلم",url="https://t.me/H_P_K")
		de = types.InlineKeyboardButton(text="دراكون",url="https://t.me/s_l_3")
		ch = types.InlineKeyboardButton(text="▶ قناة البوت ◀",url="https://t.me/c_p_8")
		rr.add(me,he,de)
		rr.add(ch)
		bot.send_message(message.chat.id,text="هذا البوت مدفوع وليس لك\n للتفعيل راسل",reply_markup=rr)
               
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	if call.data =="K_8_U":
		
		mas = types.InlineKeyboardMarkup(row_width=2)
		
		A = types.InlineKeyboardButton(text ="(KKKK4)", callback_data="F1")

		E = types.InlineKeyboardButton(text ="(FF8FF)", callback_data="F2")
		
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		
		F = types.InlineKeyboardButton(text ="(UUU4UU)", callback_data="F7")
		
		M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
		
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
	elif call.data == "SS":
		v = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(Q_8_P)", callback_data="F3")
		J = types.InlineKeyboardButton(text ="(N_G_6)", callback_data="F4")
		I = types.InlineKeyboardButton(text ="(B_5_7)", callback_data="F5")
		O = types.InlineKeyboardButton(text ="(I_C_E)", callback_data="F6")
		S = types.InlineKeyboardButton(text ="(G_K_K)", callback_data="F10")
		B = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		v.add(K,J,O,I,S)
		v.add(B)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=v)
	elif call.data =="F1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xa = "1234567890"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			us1 = str(us)+str(us)+str(us)+str(us)+str(ua)
			us2 = str(us)+str(us)+str(us)+str(ua)+str(us)
			us3 = str(us)+str(us)+str(ua)+str(us)+str(us)
			us4 = str(us)+str(ua)+str(us)+str(us)+str(us)
			d = [us1,us2,us3,us4]
			h = random.choice(d)
			url = "https://t.me/"+h
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and d not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{h}\n────── • ✧✧ • ──────\n•مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{h}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
			
	elif call.data =="F8":
		e = types.InlineKeyboardMarkup(row_width=2)
		f = types.InlineKeyboardButton(text="(c8bot)",callback_data="b1")
		c = types.InlineKeyboardButton(text="(vd2bot)",callback_data="b2")
		z = types.InlineKeyboardButton(text="(wdv4bot)",callback_data="b4")
		bc = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		e.add(f,c,z)
		e.add(bc)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=e)
	elif call.data =="F100":
		e = types.InlineKeyboardMarkup(row_width=2)
		f = types.InlineKeyboardButton(text="(vv_vv)",callback_data="ew1")
		c = types.InlineKeyboardButton(text="(UUU4UU)",callback_data="F7")
		d = types.InlineKeyboardButton(text="(FFAAA)",callback_data="ew")
		z = types.InlineKeyboardButton(text="(KKKK4)",callback_data="F1")
		bc = types.InlineKeyboardButton(text="رجوع",callback_data="bckkk")
		e.add(f,c,z,d)
		e.add(bc)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="اختر من القائمه بالاسفل .",reply_markup=e)
	elif call.data =="bckkk":
		mas = types.InlineKeyboardMarkup(row_width=2)
		K = types.InlineKeyboardButton(text ="(يوزرات ثلاثيه)", callback_data="SS")	
		G = types.InlineKeyboardButton(text ="(يوزرات بوتات)", callback_data="F8")
		V = types.InlineKeyboardButton(text ="(يوزرات مميزه)", callback_data="F100")
		M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
		mas.add(G,K)
		mas.add(V)
		mas.add(M)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="- أهلاً بكً عزيزي المستخدم \n\n- بوت تشكير يوزرات تلجرام 🧑‍💻\n\n♻️ لوحة التحكم الخاصه بك ♨️",reply_markup=mas)
		
	
	elif call.data =="b4":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(u1s)+str(u2s)+str(un)+"bot"
			u2 = str(us)+str(un)+str(u2s)+str(u1s)+"bot"
			u3 = str(us)+str(u1s)+str(un)+str(u2s)+"bot"
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	
	elif call.data =="ew1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(us)+"_"+str(us)+str(us)
			u2= str(us)+"_"+str(us)+str(us)+str(us)
			u3= str(us)+str(us)+str(us)+"_"+str(us)
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="ew":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(us)+str(us)+str(u1s)+str(u1s)
			u2= str(u1s)+str(u1s)+str(us)+str(us)+str(us)
			g = [u1,u2]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="b2":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(u1s)+str(un)+"bot"
			u2 = str(us)+str(u1s)+str(u2s)+"bot"
			u3 = str(us)+str(un)+str(u1s)+"bot"
			g = [u1,u2,u3]
			x = random.choice(g)
			url = "https://t.me/"+x
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and g not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{x}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{x}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	
		
	elif call.data =="b1":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			u1= str(us)+str(un)+"bot"
			u2 = str(us)+str(u1s)+"bot"
			f = [u1,u2]
			v = random.choice(f)
			url = "https://t.me/"+v
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and f not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{v}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{v}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F6":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(u1s)+"_"+str(u2s)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F5":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(un)+"_"+str(u1n)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F4":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(u1s)+"_"+str(un)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F3":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(un)+"_"+str(u1s)
			url = "https://t.me/"+c
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and c not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{c}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{c}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	elif call.data =="F7":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			h1 = str(us)+str(un)+str(us)+str(us)+str(us)+str(us)
			h2 = str(us)+str(us)+str(un)+str(us)+str(us)+str(us)
			h3 = str(us)+str(us)+str(us)+str(un)+str(us)+str(us)
			h4 = str(us)+str(us)+str(us)+str(us)+str(un)+str(us)
			h5 = str(us)+str(us)+str(us)+str(us)+str(us)+str(un)
			K_8_U = [h1,h2,h3,h4,h5]
			j = random.choice(K_8_U)
			url = "https://t.me/"+j
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and j not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{j}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{j}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				K_8_U = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,K_8_U)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
	elif call.data =="F10":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xn = "1234567890"
		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		while True:
			us = str(''.join(random.choice(xu)for i in range(1)))
			u2s = str(''.join(random.choice(xu)for i in range(1)))
			u1s = str(''.join(random.choice(xu)for i in range(1)))
			un = str(''.join(random.choice(xn)for i in range(1)))
			u1n = str(''.join(random.choice(xn)for i in range(1)))
			ua = str(''.join(random.choice(xa)for i in range(1)))
			c = str(us)+"_"+str(us)+"_"+str(u2s)
			d = str(u1s)+"_"+str(us)+"_"+str(us)
			v = str(us)+"_"+str(u1s)+"_"+str(us)
			p = str(us)+"_"+str(un)+"_"+str(us)
			m = str(us)+"_"+str(us)+"_"+str(un)
			i = str(us)+"_"+str(un)+"_"+str(un)
			cs = [c,d,v,p,m,i]
			cc = random.choice(cs)
			url = "https://t.me/"+cc
			headers = {
            "User-Agent": generate_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = requests.get(url, headers=headers)
			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0 and cs not in ban:
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f"‹ يوزرات تلي متاحه ✓\n────── • ✧✧ • ──────\n‹ صدتلك يوزر : @{cc}\n────── • ✧✧ • ──────\n• مطور البوت @K_8_U")
				
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{cc}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('DEV', url='https://t.me/K_8_U')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
  
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://"+ Heroku +".herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
