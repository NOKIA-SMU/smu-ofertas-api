''' TIPO_ACCESO_CHOICES '''
URBANO = 'URBANO '
RURAL = 'RURAL'
ACCESODIFICIL = 'ACCESO DIFICIL'
FLUVIAL = 'FLUVIAL'
AEREO = 'AEREO'
COMUNIDADINDIGENA = 'COMUNIDAD INDIGENA'
TIPO_ACCESO_CHOICES = (
    (URBANO, 'URBANO'),
    (RURAL, 'RURAL'),
    (ACCESODIFICIL, 'ACCESO DIFICIL'),
    (FLUVIAL, 'FLUVIAL'),
    (AEREO, 'AEREO'),
    (COMUNIDADINDIGENA, 'COMUNIDAD INDIGENA'),
)

''' NATURALEZA_SERVICIO_CHOICES '''
PREVENTIVO = 'PREVENTIVO'
CORRECTIVO = 'CORRECTIVO'
EMERGENCIA = 'EMERGENCIA'
INTEGRAL = 'INTEGRAL'
PREDICTIVO = 'PREDICTIVO'
NATURALEZA_SERVICIO_CHOICES = (
    (PREVENTIVO, 'PREVENTIVO'),
    (CORRECTIVO, 'CORRECTIVO'),
    (EMERGENCIA, 'EMERGENCIA'),
    (INTEGRAL, 'INTEGRAL'),
    (PREDICTIVO, 'PREDICTIVO'),
)

''' TIPO_OFERTA_CHOICES '''
SMU = 'SMU'
BACKLOG = 'BACKLOG'
HURTO = 'HURTO'
TIPO_OFERTA_CHOICES = (
    (SMU, 'SMU'),
    (BACKLOG, 'BACKLOG'),
    (HURTO, 'HURTO'),
)

''' TIPO_ELEMENTO_CHOICES '''
CAPEX = 'CAPEX'
OPEX = 'OPEX'
TIPO_ELEMENTO_CHOICES = (
    (CAPEX, 'CAPEX'),
    (OPEX, 'OPEX'),
)

''' MODALIDAD_CHOICES '''
LPU = 'LPU'
APU = 'APU'
FEE = 'FEE'
MODALIDAD_CHOICES = (
    (LPU, 'LPU'),
    (APU, 'APU'),
    (FEE, 'FEE'),
)

''' TIPO_ADQUISICION_CHOICES '''
PROVEEDOR = 'PROVEEDOR'
PERSONALNOKIA = 'PERSONAL NOKIA'
BODEGA = 'BODEGA'
COMPRALOCAL = 'COMPRA LOCAL'
INTERMEDIARIO = 'INTERMEDIARIO'
PALABRERO = 'PALABRERO'
TIPO_ADQUISICION_CHOICES = (
    (PROVEEDOR, 'PROVEEDOR'),
    (PERSONALNOKIA, 'PERSONAL NOKIA'),
    (BODEGA, 'BODEGA'),
    (COMPRALOCAL, 'COMPRA LOCAL'),
    (INTERMEDIARIO, 'INTERMEDIARIO'),
    (PALABRERO, 'PALABRERO'),
)

''' PROVEEDOR_CHOICES '''
CUMMINSDELOSANDES = 'CUMMINS DE LOS ANDES'
METRICOM = 'METRICOM'
BIOTECNICA = 'BIOTECNICA'
CASAINGLESA = 'CASA INGLESA'
CONECTAR = 'CONECTAR'
DECOM = 'DECOM'
ELECTRICOSSURAMERICA = 'ELECTRICOS SURAMERICA'
ELTEK = 'ELTEK'
FERNEYGUTIERREZ = 'FERNEY GUTIERREZ'
INGYTELCOM = 'INGYTELCOM'
MICROLINK = 'MICROLINK'
NESITELCO = 'NESITELCO'
OSC = 'OSC'
MSI = 'MSI'
PRODATEL = 'PRODATEL'
SELLING = 'SELLING'
SUSEQUID = 'SUSEQUID'
TRS = 'TRS'
UNIONELECTRICA = 'UNION ELECTRICA'
CAJOS = 'CAJOS'
PROVEEDOR_CHOICES = (
    (CUMMINSDELOSANDES, 'CUMMINS DE LOS ANDES'),
    (METRICOM, 'METRICOM'),
    (BIOTECNICA, 'BIOTECNICA'),
    (CASAINGLESA, 'CASA INGLESA'),
    (CONECTAR, 'CONECTAR'),
    (DECOM, 'DECOM'),
    (ELECTRICOSSURAMERICA, 'ELECTRICOS SURAMERICA'),
    (ELTEK, 'ELTEK'),
    (FERNEYGUTIERREZ, 'FERNEY GUTIERREZ'),
    (INGYTELCOM, 'INGYTELCOM'),
    (MICROLINK, 'MICROLINK'),
    (NESITELCO, 'NESITELCO'),
    (OSC, 'OSC'),
    (MSI, 'MSI'),
    (PRODATEL, 'PRODATEL'),
    (SELLING, 'SELLING'),
    (SUSEQUID, 'SUSEQUID'),
    (TRS, 'TRS'),
    (UNIONELECTRICA, 'UNION ELECTRICA'),
    (CAJOS, 'CAJOS'),
)

''' TIPO_RESPUESTA_CLIENTE_CHOICES '''
APROBADO = 'APROBADO'
RECHAZADO = 'RECHAZADO'
APROBADOMENORVALOR = 'APROBADO MENOR VALOR'
SINRESPUESTA = 'SIN RESPUESTA'
TIPO_RESPUESTA_CLIENTE_CHOICES = (
    (APROBADO, 'APROBADO'),
    (RECHAZADO, 'RECHAZADO'),
    (APROBADOMENORVALOR, 'APROBADO MENOR VALOR'),
    (SINRESPUESTA, 'SIN RESPUESTA'),
)

''' CONFIRMACION_RECIBIDO_CHOICES '''
SI = 'SI'
NO = 'NO'
PENDIENTE = 'PENDIENTE'
CONFIRMACION_RECIBIDO_CHOICES = (
    (SI, 'SI'),
    (NO, 'NO'),
    (PENDIENTE, 'PENDIENTE'),
)

''' SUBESTADO_OFERTA_CHOICES '''
PENDIENTEPO = 'PENDIENTE PO'
PENDIENTEAPROBACIONCOMPRASCLARO = 'PENDIENTE APROBACION COMPRAS CLARO'
PENDIENTEAPROBACIONZONACLARO = 'PENDIENTE APROBACION ZONA CLARO'
PENDIENTEEJECUCION = 'PENDIENTE EJECUCION'
SOLICITUDCANCELADA = 'SOLICITUD CANCELADA'
SUMINISTROENIMPORTACION = 'SUMINISTRO EN IMPORTACION'
NOAPROBADOPORCOMPRASNOKIAPORMENORVALOR = 'NO APROBADO POR COMPRAS NOKIA POR MENOR VALOR'
RECIBIDODESUPERVISOR = 'RECIBIDO DE SUPERVISOR'
ENREVISIONANALISTAOFERTASNOKIA = 'EN REVISION ANALISTA OFERTAS NOKIA'
ENPROCESODECOTIZACIONPROVEEDORES = 'EN PROCESO DE COTIZACION PROVEEDORES'
SUBESTADO_OFERTA_CHOICES = (
    (PENDIENTEPO, 'PENDIENTE PO'),
    (PENDIENTEAPROBACIONCOMPRASCLARO, 'PENDIENTE APROBACION COMPRAS CLARO'),
    (PENDIENTEAPROBACIONZONACLARO, 'PENDIENTE APROBACION ZONA CLARO'),
    (PENDIENTEEJECUCION, 'PENDIENTE EJECUCION'),
    (SOLICITUDCANCELADA, 'SOLICITUD CANCELADA'),
    (SUMINISTROENIMPORTACION, 'SUMINISTRO EN IMPORTACION'),
    (NOAPROBADOPORCOMPRASNOKIAPORMENORVALOR, 'NO APROBADO POR COMPRAS NOKIA POR MENOR VALOR'),
    (RECIBIDODESUPERVISOR, 'RECIBIDO DE SUPERVISOR'),
    (ENREVISIONANALISTAOFERTASNOKIA, 'EN REVISION ANALISTA OFERTAS NOKIA'),
    (ENPROCESODECOTIZACIONPROVEEDORES, 'EN PROCESO DE COTIZACION PROVEEDORES'),
)

''' ESTADO_OFERTA_CHOICES '''
PENDIENTEEJECUCION = 'PENDIENTE EJECUCION'
PENDIENTECOTIZACIONPROVEEDOR = 'PENDIENTE COTIZACION PROVEEDOR'
PENDIENTEPO = 'PENDIENTE PO'
SINPROCESAR = 'SIN PROCESAR'
SOLICITUDCANCELADA = 'SOLICITUD CANCELADA'
PENDIENTEAPROBACIONCLARO = 'PENDIENTE APROBACION CLARO'
ESTADO_OFERTA_CHOICES = (
    (PENDIENTEEJECUCION, 'PENDIENTE EJECUCION'),
    (PENDIENTECOTIZACIONPROVEEDOR, 'PENDIENTE COTIZACION PROVEEDOR'),
    (PENDIENTEPO, 'PENDIENTE PO'),
    (SINPROCESAR, 'SIN PROCESAR'),
    (SOLICITUDCANCELADA, 'SOLICITUD CANCELADA'),
    (PENDIENTEAPROBACIONCLARO, 'PENDIENTE APROBACION CLARO'),
)
