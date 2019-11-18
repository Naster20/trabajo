# PROGRAMA 1° CALCULAR PROMEDIO
#DECLARACION
nota1=0.0
nota2=0.0
nota3=0.0
promedio=0.0
#IMPUT
nota1=15.3
nota2=16.6
nota3=19.0
#PROCESSING
promedio=((nota1+nota2+nota3)/3)
#OUTPUT
print("PROMEDIO=",promedio)
# PROGRAMA 2° CALCULAR EL DESCUENTO
#DECLARACION
precio1=0.0
precio2=0.0
precio3=0.0
descuento=0.0
total=0.0
total_pagar=0.0
#IMPUT
precio1=320.0
precio2=160.0
precio3=240.0
descuento=0.40
total=0.0
total_pagar=0.0
#PROCESSING
total=(precio1+precio2+precio3)
descuento=(total)*descuento
total_pagar=(total-descuento)
#OUTPUT
print("TOTAL =",total)
print("DESCUENTO =",descuento)
print("TOTAL A PAGAR =",total_pagar)
## PROGRAMA 3° CALCULAR EL TOTAL DE VENTAS NETAS
#DECLARACION
ventas_netas2005=0.0
ventas_netas2006=0.0
ventas_netas2007=0.0
ventas_netas2008=0.0
total_ventas_netas=0.0
#IMPUT
ventas_netas2005=15321
ventas_netas2006=18249
ventas_netas2007=20893
ventas_netas2008=20131
total_ventas_netas=0.0
#PROCESSING
total_ventas_netas=(ventas_netas2005+ventas_netas2006+ventas_netas2007+ventas_netas2008)
#OUTPUT
print("TOTAL DE VENTAS NETAS =",total_ventas_netas)
# PROGRAMA 4° CALCULAR INDICE DE MASA CORPORAL
#DECLARACION
talla=0.0
peso=0.0
indice_de_masa_corporal=0.0
#IMPUT
talla=1.65
peso=83
indice_de_masa_corporal=0.0
#PROCESSING
indice_de_masa_corporal=(peso/(talla)**2)
#OUTPUT
print("INDICE DE MASA CORPORAL =",indice_de_masa_corporal)
# PROGRAMA 5° CALCULAR EL IGV DEL TOTAL DE VENTAS NETAS
#DECLARACION
igv=0.0
#IMPUT
igv=0.0
#PROCESSING
igv=(total_ventas_netas)*0.18
#OUTPUT
print("IGV DE VENTAS NETAS =",igv)
# PROGRAMA 6° FACTURA
#DECLARACION
soporte_tecnico=0.0
reparacion_smartphone=0.0
venta_mouse=0.0
venta_teclado_supra=0.0
venta_pantalla_l32=0.0
memoria_usb_132GB=0.0
total_base_imponible=0.0
iva=0.0
retencion=0.0
Total_1=0.0
#IMPUT
soporte_tecnico=80.00
reparacion_smartphone=35.00
venta_mouse=10.00
venta_teclado_supra=25.00
venta_pantalla_l32=60.00
memoria_usb_132GB=20.00
total_base_imponible=0.0
iva=0.0
retencion=0.0
Total_1=0.0
#PROCESSING
total_base_imponible=(soporte_tecnico+reparacion_smartphone+venta_mouse+venta_teclado_supra+venta_pantalla_l32+memoria_usb_132GB)
iva=(total_base_imponible)*0.21
retencion=((total_base_imponible)*(0.15))
total_1=((total_base_imponible)+(iva)-(retencion))
#OUTPUT
print("TOTAL BASE IMPONIBLE =",total_base_imponible)
print("I.V.A. 21% =",iva)
print("RETENCION 15% =",retencion)
print("TOTAL =",total_1)
# PROGRAMA 7° GASTOS DE OPERACION
#DECLARACION
gastos_operacion_2005=0.0
gastos_operacion_2006=0.0
gastos_operacion_2007=0.0
total_de_gastes_en_operaciones=0.0
#IMPUT
gastos_operacion_2005=3563.0
gastos_operacion_2006=3655.0
gastos_operacion_2007=4130.0
total_de_gastes_en_operaciones=0.0
#PROCESSING
total_de_gastes_en_operaciones=(gastos_operacion_2005+gastos_operacion_2006+gastos_operacion_2007)
#OUTPUT
print("GASTO TOTAL DE OPERACIONES =",total_de_gastes_en_operaciones)
# PROGRAMA 8° DIVIDENDOS POR CPO
#DECLARACION
dividendos_por_cpo_2005=0.0
dividendos_por_cpo_2006=0.0
dividendos_por_cpo_2007=0.0
total_de_dividendos_por_cpo=0.0
#IMPUT
dividendos_por_cpo_2005=0.06
dividendos_por_cpo_2006=0.09
dividendos_por_cpo_2007=0.08
total_de_dividendos_por_cpo=0.0
#PROCESSING
total_de_dividendos_por_cpo=(dividendos_por_cpo_2005+dividendos_por_cpo_2006+dividendos_por_cpo_2007)
#OUTPUT
print("TOTAL DE DIVIDENDOS POR CPO =",total_de_dividendos_por_cpo)
# PROGRAMA °9 TOTAL PASIVO
#DECLARACION
total_pasivo_2005=0.0
total_pasivo_2006=0.0
total_pasivo_2007=0.0
total_pasivo_2008=0.0
total_pasivo=0.0
#IMPUT
total_pasivo_2005=16409.0
total_pasivo_2006=15139.0
total_pasivo_2007=30967.0
total_pasivo_2008=28119.0
total_pasivo=0.0
#PROCESSING
total_pasivo=(total_pasivo_2005+total_pasivo_2006+total_pasivo_2007+total_pasivo_2008)
#OUTPUT
print("TOTAL PASIVO (2005-2008) =",total_pasivo)
# PROGRAMA °10 CAPITAL DE TRABAJO NETO
#DECLARACION
capital_de_trabajo_neto_2005=0.0
capital_de_trabajo_neto_2006=0.0
capital_de_trabajo_neto_2007=0.0
capital_de_trabajo_neto_2008=0.0
total_trabajo_neto=0.0
#IMPUT
capital_de_trabajo_neto_2005=1268.0
capital_de_trabajo_neto_2006=887.0
capital_de_trabajo_neto_2007=1383.0
capital_de_trabajo_neto_2008=1191.0
total_trabajo_neto=0.0
#PROCESSING
total_trabajo_neto=(capital_de_trabajo_neto_2005+capital_de_trabajo_neto_2006+capital_de_trabajo_neto_2007+capital_de_trabajo_neto_2008)
#OUTPUT
print("TOTAL DE TRABAJO NETO (2005-2008) =",total_trabajo_neto)
# PROGRAMA °11 UTILIDAD PERDIDA POR CPO
#DECLARACION
utilidad_perdida_por_cpo2005=0.0
utilidad_perdida_por_cpo2006=0.0
utilidad_perdida_por_cpo2007=0.0
utilidad_perdida_por_cpo2008=0.0
total_utilidad_perdida_por_cpo=0.0
#IMPUT
utilidad_perdida_por_cpo2005=0.31
utilidad_perdida_por_cpo2006=0.33
utilidad_perdida_por_cpo2007=0.32
utilidad_perdida_por_cpo2008=0.02
total_utilidad_perdida_por_cpo=0.0
#PROCESSING
total_utilidad_perdida_por_cpo=(utilidad_perdida_por_cpo2005+utilidad_perdida_por_cpo2006+utilidad_perdida_por_cpo2007+utilidad_perdida_por_cpo2008)
#OUTPUT
print("TOTAL DE UTILIDAD PERDIDA POR CPO (2005-2008) =",total_utilidad_perdida_por_cpo)
# PROGRAMA °12 GASTOS FINANCIEROS
#DECLARACION
gasto_financiero_2005=0.0
gasto_financiero_2006=0.0
gasto_financiero_2007=0.0
gasto_financiero_2008=0.0
total_gastos_financieros=0.0
#IMPUT
gasto_financiero_2005=526
gasto_financiero_2006=494
gasto_financiero_2007=807
gasto_financiero_2008=910
total_gastos_financieros=0.0
#PROCESSING
total_gastos_financieros=(gasto_financiero_2005+gasto_financiero_2006+gasto_financiero_2007+gasto_financiero_2008)
#OUTPUT
print("TOTAL DE GASTOS FINANCIEROS (2005-2008) =",total_gastos_financieros)
# PROGRAMA °13 BOLETA DE VENTA
#DECLARACION
libro_auditoria_tributaria=0.0
libro_manual_del_contador=0.0
compendio_laboral_2013=0.0
Total_boleta=0.0
#IMPUT
libro_auditoria_tributaria=250.0
libro_manual_del_contador=250.0
compendio_laboral_2013=300.0
total_boleta=0.0
#PROCESSING
total_boleta=(libro_auditoria_tributaria+libro_manual_del_contador+compendio_laboral_2013)
#OUTPUT
print("TOTAL DE LA BOLETA = ",total_boleta)
# PROGRAMA °14 COSTO DE VENTAS
#DECLARACION
costo_ventas_2005=0.0
costo_ventas_2006=0.0
costo_ventas_2007=0.0
costo_ventas_2008=0.0
costo_total=0.0
#IMPUT
costo_ventas_2005=9271
costo_ventas_2006=11649
costo_ventas_2007=13868
costo_ventas_2008=13735
costo_total=0.0
#PROCESSING
costo_total=(costo_ventas_2005+costo_ventas_2006+costo_ventas_2007+costo_ventas_2008)
#OUTPUT
print("COSTO TOTAL DE VENTAS = ",costo_total)
# PROGRAMA °15 OTROS GASTOS
#DECLARACION
otros_gastos_2005=0.0
otros_gastos_2006=0.0
otros_gastos_2007=0.0
otros_gastos_2008=0.0
total_de_otros_gastos=0.0
#IMPUT
otros_gastos_2005=316
otros_gastos_2006=49
otros_gastos_2007=273
otros_gastos_2008=1909
total_de_otros_gastos=0.0
#PROCESSING
total_de_otros_gastos=(otros_gastos_2005+otros_gastos_2006+otros_gastos_2007+otros_gastos_2008)
#OUTPUT
print("TOTAL DE OTROS GASTOS =",total_de_otros_gastos)
# PROGRAMA °16 UTILIDAD BRUTA
#DECLARACION
utilidad_bruta_2005=0.0
utilidad_bruta_2006=0.0
utilidad_bruta_2007=0.0
total_de_utilidad_bruta=0.0
#IMPUT
utilidad_bruta_2005=6050
utilidad_bruta_2006=6600
utilidad_bruta_2007=7025
total_de_utilidad_bruta=0.0
#PROCESSING
total_de_utilidad_bruta=(utilidad_bruta_2005+utilidad_bruta_2006+utilidad_bruta_2007)
#OUTPUT
print("TOTAL DE UTILIDAD BRUTA =",total_de_utilidad_bruta)
# PROGRAMA °17 FLUJO DE OPERACION
#DECLARACION
flujo_de_operacion_2005=0.0
flujo_de_operacion_2006=0.0
flujo_de_operacion_2007=0.0
total_flujo_de_operacion=0.0
#IMPUT
flujo_de_operacion_2005=3557
flujo_de_operacion_2006=4138
flujo_de_operacion_2007=4512
total_flujo_de_operacion=0.0
#PROCESSING
total_flujo_de_operacion=(flujo_de_operacion_2005+flujo_de_operacion_2006+flujo_de_operacion_2007)
#OUTPUT
print("TOTAL DEL FLUJO DE OPERACION =",total_flujo_de_operacion)
# PROGRAMA °18 TOTAL DE CAPITAL CONTABLE
#DECLARACION
capital_contable_2005=0.0
capital_contable_2006=0.0
capital_contable_2007=0.0
total_capital_contable=0.0
#IMPUT
capital_contable_2005=10354
capital_contable_2006=14779
capital_contable_2007=18695
total_capital_contable=0.0
#PROCESSING
total_capital_contable=(capital_contable_2005+capital_contable_2006+capital_contable_2007)
#OUTPUT
print("TOTAL DEL CAPITAL CONTABLE =",total_capital_contable)
# PROGRAMA °19 PARTICIPACION CONTROLADORA
#DECLARACION
participacion_controladora_2005=0.0
participacion_controladora_2006=0.0
participacion_controladora_2007=0.0
total_participacion_controladora=0.0
#IMPUT
participacion_controladora_2005=9825
participacion_controladora_2006=12859
participacion_controladora_2007=14942
total_participacion_controladora=0.0
#PROCESSING
total_participacion_controladora=(participacion_controladora_2005+participacion_controladora_2006+participacion_controladora_2007)
#OUTPUT
print("TOTAL DE PARTICIPACION CONTROLADORA =",total_participacion_controladora)
# PROGRAMA °20
#DECLARACION
valor_en_libros_por_cpo_2005=0.0
valor_en_libros_por_cpo_2006=0.0
valor_en_libros_por_cpo_2007=0.0
valor_en_libros_por_cpo_2008=0.0
total_de_valor_en_libros_por_cpo=0.0
#IMPUT
valor_en_libros_por_cpo_2005=1.39
valor_en_libros_por_cpo_2006=1.75
valor_en_libros_por_cpo_2007=1.99
valor_en_libros_por_cpo_2008=1.63
total_de_valor_en_libros_por_cpo=0.0
#PROCESSING
total_de_valor_en_libros_por_cpo=(valor_en_libros_por_cpo_2005+valor_en_libros_por_cpo_2006+valor_en_libros_por_cpo_2007+valor_en_libros_por_cpo_2008)
#OUTPUT
print("TOTAL DE VALOR EN LIBROS POR CPO =",total_de_valor_en_libros_por_cpo)
FileNotFoundError
