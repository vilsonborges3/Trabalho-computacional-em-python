#Vilson Borges - 12011EAU020
#Leonardo Silva Vieira - 11821EEL008
#CIRCUITOS TRIFÁSICOS DESEQUILIBRADOS - Y
import os
import numpy as np
import matplotlib.pyplot as plt



os.system('cls')
print("                     ********************************")
print("                 CIRCUITOS TRIFÁSICOS DESEQUILIBRADOS - Y")
print("               ********************************************* \n")

#OPÇÃO PRA DEFINIR A ENTRADA DOS DADOS
num = int(input('Digite:\n1 Para circuito 4 fios \n2 Para circuito 3 fios \n3 Para abrir relatorio desse codigo   \n\n->>>'))
fr = 60
omega = 2*np.pi*fr
#VERIFICAÇÃO DOS DADOS ENTRADOS
if (num == 1):
  os.system('cls')
  #ENTRADA DAS VARIÁVEIS
  za = complex(float(input("Digite a parte real de za ->>> ")), float(input("Digite a parte imaginária de za ->>> ")))
  zb = complex(float(input("Digite a parte real de zb ->>> ")), float(input("Digite a parte imaginária de zb ->>> ")))
  zc = complex(float(input("Digite a parte real de zc ->>> ")), float(input("Digite a parte imaginária de zc ->>> ")))

  va = float(input("\n\nDigite o modulo de Va ->>>"))*np.exp(1j*np.deg2rad(float(input("Digite a fase de Va ->>>"))))
  vb = float(input("Digite o modulo de Vb ->>> "))*np.exp(1j*np.deg2rad(float(input("Digite a fase de Vb ->>>"))))
  vc = float(input("Digite o modulo de Vc ->>> "))*np.exp(1j*np.deg2rad(float(input("Digite a fase de Vc ->>>"))))
  
  vab = vb - va
  vbc = vc - vb
  vca = va - vc

  fr = float(input("\n\nDigite a frequencia da fonte ->>>  "))
  cic = float(input("\n\nDigite o numero de ciclos dos graficos ->>>  "))
  

  os.system('cls')
  print('\n>>>>RESULTADOS<<<<')
  ia = va/za
  print(" ou ia: " + str(ia) + "A," + str(np.abs(ia)) + " <" + str((np.angle(ia) * 180)/np.pi) + "A")
  ib = vb/zb
  print("ib: " + str(ib) + "A, ou " + str(np.abs(ib)) + " <" + str((np.angle(ib) * 180)/np.pi) + "A")
  ic = vc/zc
  print("ic: " + str(ic) + "A, ou " + str(np.abs(ic)) + " <" + str((np.angle(ic) * 180)/np.pi) + "A")

  i_n = -(ia + ib + ic)
  print("in: " + str(i_n) + "A, ou " + str(np.abs(i_n)) + " <" + str((np.angle(i_n) * 180)/np.pi) + "A")

   

  print("\n<Potências complexas/>")
  sa=(np.abs(ia)**2)*za
  print("Sa: " + str(sa) + "VA")
  print("Onde: Potência ativa = " + str(sa.real) + "w" )
  print("E, Potência reativa = " + str(sa.imag) + "Va \n\n" )
  fpa = sa.real/np.abs(sa)
  print("E, fator de potencia= " + str(fpa) + " \n\n" )

  sb=(np.abs(ib)**2)*zb
  print("Sb: " + str(sb) + "VA")
  print("Onde: Potência ativa = " + str(sb.real) + "w" )
  print("E, Potência reativa = " + str(sb.imag) + "Va \n\n" )
  fpb = sb.real/np.abs(sb)
  print("E, fator de potencia= " + str(fpb) + " \n\n" )

  sc=(np.abs(ic)**2)*zc
  print("Sc: " + str(sc) + "VA")
  print("Onde: Potência ativa = " + str(sc.real) + "w" )
  print("E, Potência reativa = " + str(sc.imag) + "Va \n\n" )
  fpc = sc.real/np.abs(sc)
  print("E, fator de potencia= " + str(fpc) + " \n\n" )

  st = sa + sb + sc
  fp = st.real/np.abs(st)
  print("ST: " + str(st) + "VA")
  print("Onde: Potência ativa total = " + str(st.real) + "w" )
  print("Potência reativa total = " + str(st.imag) + "VAq \n\n" )
  print("E, fator de potencia= " + str(fp) + " \n\n" )

  #plotagem das tensões de linha
  time = np.arange(0.0000, (1/fr)*cic, 0.0001)
  plt.plot(time, (np.abs(va))*(np.sin(omega*time + ((np.angle(va) * 180)/np.pi))), 'r', label='Va')
  plt.plot(time, (np.abs(vb))*(np.sin(omega*time + ((np.angle(vb) * 180)/np.pi))), 'g', label='Vb' )
  plt.plot(time, (np.abs(vc))*(np.sin(omega*time + ((np.angle(vc) * 180)/np.pi))), 'b', label='Vc' )
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Tensão [v]")
  plt.title("Tensões de linha")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem das tensões de fase
  time = np.arange(0.0000, (1/fr)*cic, 0.0001)
  plt.plot(time, (np.abs(vab))*(np.sin(omega*time + ((np.angle(vab) * 180)/np.pi))), 'r', label='Vab')
  plt.plot(time, (np.abs(vbc))*(np.sin(omega*time + ((np.angle(vbc) * 180)/np.pi))), 'g', label='Vbc' )
  plt.plot(time, (np.abs(vca))*(np.sin(omega*time + ((np.angle(vca) * 180)/np.pi))), 'b', label='Vca' )
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Tensão [v]")
  plt.title("Tensões de fase")
  plt.legend(loc='upper right')
  plt.show()

  #plotagem das correntes de linha
  plt.plot(time, (np.abs(ia))*(np.sin(omega*time + ((np.angle(ia) * 180)/np.pi))), 'r', label='Ia')
  plt.plot(time, (np.abs(ib))*(np.sin(omega*time + ((np.angle(ib) * 180)/np.pi))), 'g', label='Ib')
  plt.plot(time, (np.abs(ic))*(np.sin(omega*time + ((np.angle(ic) * 180)/np.pi))), 'b', label='Ic')
  plt.plot(time, (np.abs(i_n))*(np.sin(omega*time + ((np.angle(i_n) * 180)/np.pi))), 'm', label='In')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Corrente [A]")
  plt.title("Correntes de linha")
  plt.legend(loc='upper right')  
  plt.show()

  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(ia))*(np.sin(omega*time + ((np.angle(ia) * 180)/np.pi))), 'r', label='Ia')
  plt.grid(True)
  plt.title("Correntes de linha")
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right') 

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(ib))*(np.sin(omega*time + ((np.angle(ib) * 180)/np.pi))), 'g', label='Ib')
  plt.grid(True)
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right') 

  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(ic))*(np.sin(omega*time + ((np.angle(ic) * 180)/np.pi))), 'b', label='Ic')
  plt.grid(True)
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right') 

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(i_n))*(np.sin(omega*time + ((np.angle(i_n) * 180)/np.pi))), 'm', label='In')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem da potencia aparente
  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(sa))*((np.sin(omega*time)**2)) + ((np.angle(sa) * 180)/np.pi), 'r', label='Sa')
  plt.plot(time, (np.abs(sb))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'g', label='Sb')
  plt.plot(time, (np.abs(sc))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'b', label='Sc')
  plt.grid(True)
  plt.ylabel("S [VA]")
  plt.title("Potencia Aparente")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(sa))*((np.sin(omega*time)**2)) + ((np.angle(sa) * 180)/np.pi), 'r', label='Sa')
  plt.grid(True)
  plt.ylabel("S [VA]")
  plt.legend(loc='upper right')
  
  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(sb))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'g', label='Sb')
  plt.grid(True)
  plt.ylabel("S [VA]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(sc))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'b', label='Sc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("S [VA]")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem da potencia reativa
  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(sa.imag))*(np.sin(omega*time )), 'r', label='Qa')
  plt.plot(time, (np.abs(sb.imag))*(np.sin(omega*time )), 'g', label='Qb')
  plt.plot(time, (np.abs(sc.imag))*(np.sin(omega*time )), 'b', label='Qc')
  plt.grid(True)
  plt.ylabel("Q [VAr]")
  plt.title("Potencia Reativa")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(sa.imag))*(np.sin(omega*time )), 'r', label='Qa')
  plt.grid(True)
  plt.ylabel("Q [VAr]")
  plt.legend(loc='upper right')
  
  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(sb.imag))*(np.sin(omega*time )), 'g', label='Qb')
  plt.grid(True)
  plt.ylabel("Q [VAr]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(sc.imag))*(np.sin(omega*time )), 'b', label='Qc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Q [VAr]")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem da potencia ativa
  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(sa.real))*(np.sin(omega*time )**2), 'r', label='Pa')
  plt.plot(time, (np.abs(sb.real))*(np.sin(omega*time )**2), 'g', label='Pb')
  plt.plot(time, (np.abs(sc.real))*(np.sin(omega*time )**2), 'b', label='Pc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("P [W]")
  plt.title("Potencia Ativa")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(sa.real))*(np.sin(omega*time )**2), 'r', label='Pa')
  plt.grid(True)
  plt.ylabel("P [W]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(sb.real))*(np.sin(omega*time )**2), 'g', label='Pb')
  plt.grid(True)
  plt.ylabel("P [W]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(sc.real))*(np.sin(omega*time )**2), 'b', label='Pc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("P [W]")
  plt.legend(loc='upper right')
  plt.show()
  
if (num == 2):
  os.system('cls')
  za = complex(float(input("Digite a parte real de za ->>>")), float(input("Digite a parte imaginária de za ->>>")))
  zb = complex(float(input("Digite a parte real de zb ->>>")), float(input("Digite a parte imaginária de zb ->>>")))
  zc = complex(float(input("Digite a parte real de zc ->>>")), float(input("Digite a parte imaginária de zc ->>>")))

  va = float(input("\nDigite o modulo de Va ->>>"))*np.exp(1j*np.deg2rad(float(input("Digite a fase de Va ->>>"))))
  vb = float(input("\nDigite o modulo de Vb ->>>"))*np.exp(1j*np.deg2rad(float(input("Digite a fase de Vb ->>>"))))
  vc = float(input("\nDigite o modulo de Vc ->>>"))*np.exp(1j*np.deg2rad(float(input("Digite a fase de Vc ->>>"))))

  vab = vb - va
  vbc = vc - vb
  vca = va - vc
  fr = float(input("\n\nDigite a freqencia da fonte ->>>  "))
  omega = 2*np.pi*fr
  cic = float(input("\n\nDigite o numero de ciclos dos graficos ->>>  "))
  time = np.arange(0.0000, (1/fr)*cic, 0.0001)
  
  #DECLARAÇÃO DAS MATRIZES
  a = np.array([[za + zb, -zb], [-zb, zc + zb]])
  b = np.array([[va-vb], [vb-vc]])

  #RESOLUÇÃO DA MATRIZ
  i = np.linalg.solve(a, b)
  
  ia = i[0]
  ib = i[1] - i[0]
  ic = -i[1]

  os.system('cls')
  print('\n\n>>>>RESULTADOS<<<<')
  print("ia: " + str(ia) + "A, ou " + str(np.abs(ia)) + " <" + str((np.angle(ia) * 180)/np.pi) + "A")
  print("ib: " + str(ib) + "A, ou " + str(np.abs(ib)) + " <" + str((np.angle(ib) * 180)/np.pi) + "A")
  print("ic: " + str(ic) + "A, ou " + str(np.abs(ic)) + " <" + str((np.angle(ic) * 180)/np.pi) + "A")

  i_n = -(ia + ib + ic)
  print("in: " + str(i_n) + "A, ou " + str(np.abs(i_n)) + " <" + str((np.angle(i_n) * 180)/np.pi) + "A")

  print("\n<Potências complexas/>")
  sa=(np.abs(ia)**2)*za
  print("Sa: " + str(sa) + "VA")
  print("Onde: Potência ativa = " + str(sa.real) + "w" )
  print("E, Potência reativa = " + str(sa.imag) + "Va \n\n" )
  fpa = sa.real/np.abs(sa)
  print("E, fator de potencia= " + str(fpa) + " \n\n" )

  sb=(np.abs(ib)**2)*zb
  print("Sb: " + str(sb) + "VA")
  print("Onde: Potência ativa = " + str(sb.real) + "w" )
  print("E, Potência reativa = " + str(sb.imag) + "Va \n\n" )
  fpb = sb.real/np.abs(sb)
  print("E, fator de potencia= " + str(fpb) + " \n\n" )

  sc=(np.abs(ic)**2)*zc
  print("Sc: " + str(sc) + "VA")
  print("Onde: Potência ativa = " + str(sc.real) + "w" )
  print("E, Potência reativa = " + str(sc.imag) + "Va \n\n" )
  fpc = sc.real/np.abs(sc)
  print("E, fator de potencia= " + str(fpc) + " \n\n" )

  st = sa + sb + sc
  fp = st.real/np.abs(st)
  print("ST: " + str(st) + "VA")
  print("Onde: Potência ativa total = " + str(st.real) + "w" )
  print("Potência reativa total = " + str(st.imag) + "VAq \n\n" )
  print("E, fator de potencia= " + str(fp) + " \n\n" )

  #plotagem das tensões de fase
  time = np.arange(0.0000, (1/fr)*cic, 0.0001)

  #plotagem das tensões de linha
  time = np.arange(0.0000, (1/fr)*cic, 0.0001)
  plt.plot(time, (np.abs(va))*(np.sin(omega*time + ((np.angle(va) * 180)/np.pi))), 'r', label='Va')
  plt.plot(time, (np.abs(vb))*(np.sin(omega*time + ((np.angle(vb) * 180)/np.pi))), 'g', label='Vb' )
  plt.plot(time, (np.abs(vc))*(np.sin(omega*time + ((np.angle(vc) * 180)/np.pi))), 'b', label='Vc' )
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Tensão [v]")
  plt.title("Tensões de linha")
  plt.legend(loc='upper right')
  plt.show()

  #plotagem das tensões de fase
  time = np.arange(0.0000, (1/fr)*cic, 0.0001)
  plt.plot(time, (np.abs(vab))*(np.sin(omega*time + ((np.angle(vab) * 180)/np.pi))), 'r', label='Vab')
  plt.plot(time, (np.abs(vbc))*(np.sin(omega*time + ((np.angle(vbc) * 180)/np.pi))), 'g', label='Vbc' )
  plt.plot(time, (np.abs(vca))*(np.sin(omega*time + ((np.angle(vca) * 180)/np.pi))), 'b', label='Vca' )
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Tensão [v]")
  plt.title("Tensões de fase")
  plt.legend(loc='upper right')
  plt.show()

  #plotagem das correntes de linha
  plt.plot(time, (np.abs(ia))*(np.sin(omega*time + ((np.angle(ia) * 180)/np.pi))), 'r', label='Ia')
  plt.plot(time, (np.abs(ib))*(np.sin(omega*time + ((np.angle(ib) * 180)/np.pi))), 'g', label='Ib')
  plt.plot(time, (np.abs(ic))*(np.sin(omega*time + ((np.angle(ic) * 180)/np.pi))), 'b', label='Ic')
  plt.plot(time, (np.abs(i_n))*(np.sin(omega*time + ((np.angle(i_n) * 180)/np.pi))), 'm', label='In')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Corrente [A]")
  plt.title("Correntes de linha")
  plt.legend(loc='upper right')  
  plt.show()

  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(ia))*(np.sin(omega*time + ((np.angle(ia) * 180)/np.pi))), 'r', label='Ia')
  plt.grid(True)
  plt.title("Correntes de linha")
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right') 

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(ib))*(np.sin(omega*time + ((np.angle(ib) * 180)/np.pi))), 'g', label='Ib')
  plt.grid(True)
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right') 

  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(ic))*(np.sin(omega*time + ((np.angle(ic) * 180)/np.pi))), 'b', label='Ic')
  plt.grid(True)
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right') 

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(i_n))*(np.sin(omega*time + ((np.angle(i_n) * 180)/np.pi))), 'm', label='In')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Corrente [A]")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem da potencia aparente
  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(sa))*((np.sin(omega*time)**2)) + ((np.angle(sa) * 180)/np.pi), 'r', label='Sa')
  plt.plot(time, (np.abs(sb))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'g', label='Sb')
  plt.plot(time, (np.abs(sc))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'b', label='Sc')
  plt.grid(True)
  plt.ylabel("S [VA]")
  plt.title("Potencia Aparente")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(sa))*((np.sin(omega*time)**2)) + ((np.angle(sa) * 180)/np.pi), 'r', label='Sa')
  plt.grid(True)
  plt.ylabel("S [VA]")
  plt.legend(loc='upper right')
  
  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(sb))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'g', label='Sb')
  plt.grid(True)
  plt.ylabel("S [VA]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(sc))*((np.sin(omega*time)**2)) + ((np.angle(sb) * 180)/np.pi), 'b', label='Sc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("S [VA]")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem da potencia reativa
  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(sa.imag))*(np.sin(omega*time )**2), 'r', label='Qa')
  plt.plot(time, (np.abs(sb.imag))*(np.sin(omega*time )**2), 'g', label='Qb')
  plt.plot(time, (np.abs(sc.imag))*(np.sin(omega*time )**2), 'b', label='Qc')
  plt.grid(True)
  plt.ylabel("Q [VAr]")
  plt.title("Potencia Reativa")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(sa.imag))*(np.sin(omega*time )**2), 'r', label='Qa')
  plt.grid(True)
  plt.ylabel("Q [VAr]")
  plt.legend(loc='upper right')
  
  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(sb.imag))*(np.sin(omega*time )**2), 'g', label='Qb')
  plt.grid(True)
  plt.ylabel("Q [VAr]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(sc.imag))*(np.sin(omega*time )**2), 'b', label='Qc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("Q [VAr]")
  plt.legend(loc='upper right')
  plt.show() 

  #plotagem da potencia ativa
  plt.subplot(4,1, 1)
  plt.plot(time, (np.abs(sa.real))*(np.sin(omega*time )**2), 'r', label='Pa')
  plt.plot(time, (np.abs(sb.real))*(np.sin(omega*time )**2), 'g', label='Pb')
  plt.plot(time, (np.abs(sc.real))*(np.sin(omega*time )**2), 'b', label='Pc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("P [W]")
  plt.title("Potencia Ativa")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 2)
  plt.plot(time, (np.abs(sa.real))*(np.sin(omega*time )**2), 'r', label='Pa')
  plt.grid(True)
  plt.ylabel("P [W]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 3)
  plt.plot(time, (np.abs(sb.real))*(np.sin(omega*time )**2), 'g', label='Pb')
  plt.grid(True)
  plt.ylabel("P [W]")
  plt.legend(loc='upper right')

  plt.subplot(4,1, 4)
  plt.plot(time, (np.abs(sc.real))*(np.sin(omega*time )**2), 'b', label='Pc')
  plt.grid(True)
  plt.xlabel("Tempo [s]")
  plt.ylabel("P [W]")
  plt.legend(loc='upper right')
  plt.show()

if (num == 3):
  os.startfile("relatorio.pdf")
  
if ((num != 1) & (num != 2) & (num != 3)):
  print('#########valores errados, programa será reinicado##########')
 