#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

# PORTAS
s0 = 14
s1 = 15
s2 = 2
s3 = 3
r = 0
g = 0
b = 0
output = 14
NUM_CICLOS = 10

def setup():
	GPIO.setmode(GPIO.BCM) 
	GPIO.setup(output, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(s0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(s2, GPIO.OUT)
	GPIO.setup(s3, GPIO.OUT)
	print("\n")
	
	
def detecta_vermelho():
	GPIO.output(s2, GPIO.LOW) # a cor que esse sensor detecta
	GPIO.output(s3, GPIO.LOW) # depende do sinal enviado a essas duas portas
	inicio = time.time()
	for impulso in range(NUM_CICLOS):
		GPIO.wait_for_edge(output, GPIO.FALLING)
	duracao = time.time() - inicio
	r = NUM_CICLOS / duracao
	if r > 1200:
		print('dentro da faixa vermelha')
		
	
def detecta_preto():
	GPIO.output(s2, GPIO.LOW)
	GPIO.output(s3, GPIO.HIGH)
	inicio = time.time()
	for impulso in range(NUM_CICLOS):
		GPIO.wait_for_edge(output, GPIO.FALLING)
	duracao = time.time() - inicio
	b = NUM_CICLOS / duracao
	if b < 300 and g < 300 and r < 300:
		print('dentro da faixa preta')
def detecta_verde():
	GPIO.output(s2, GPIO.HIGH)
	GPIO.output(s3, GPIO.HIGH)
	inicio = time.time()
	for impulso in range(NUM_CICLOS):
		GPIO.wait_for_edge(output, GPIO.FALLING)
	duracao = time.time() - inicio
	g = NUM_CICLOS / duracao
	if g > 900:
		print('dentro da faixa verde')

def loop(): # essa funcao parece idiota, mas se eu terminar de testar vou implementar mais funcionalidades
	detecta_vermelho()
	time.sleep(0.5)
	detecta_verde()
	time.sleep(0.5)
	detecta_preto()
	time.sleep(0.5)
	
	
if __name__ == '__main__':
	setup()
	
	while True:
		try:
			loop()
		except KeyboardInterrupt:
			print("mama eu")