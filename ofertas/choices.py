''' TIPO_SITIO_CHOICES '''
URBANO = 'URBANO'
RURAL = 'RURAL'
TIPO_SITIO_CHOICES = (
    (URBANO, 'URBANO'),
    (RURAL, 'RURAL'),
)

''' TIPO_ACCESO_CHOICES '''
ACCESODIFICIL = 'ACCESO DIFICIL'
FLUVIAL = 'FLUVIAL'
AEREO = 'AEREO'
COMUNIDADINDIGENA = 'COMUNIDAD INDIGENA'
PALABRERO = 'PALABRERO'
TIPO_ACCESO_CHOICES = (
    (URBANO, 'URBANO'),
    (ACCESODIFICIL, 'ACCESO DIFICIL'),
    (FLUVIAL, 'FLUVIAL'),
    (AEREO, 'AEREO'),
    (COMUNIDADINDIGENA, 'COMUNIDAD INDIGENA'),
    (PALABRERO, 'PALABRERO'),
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
SUMINISTRADOCLIENTE = 'SUMINISTRADO CLIENTE'
TIPO_ADQUISICION_CHOICES = (
    (PROVEEDOR, 'PROVEEDOR'),
    (PERSONALNOKIA, 'PERSONAL NOKIA'),
    (BODEGA, 'BODEGA'),
    (COMPRALOCAL, 'COMPRA LOCAL'),
    (INTERMEDIARIO, 'INTERMEDIARIO'),
    (PALABRERO, 'PALABRERO'),
    (SUMINISTRADOCLIENTE, 'SUMINISTRADO CLIENTE'),
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
NOKIA = 'NOKIA'
CLARO = 'CLARO'
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
    (NOKIA, 'NOKIA'),
    (CLARO, 'CLARO'),
)

''' TIPO_RESPUESTA_CLIENTE_CHOICES '''
APROBADO = 'APROBADO'
RECHAZADO = 'RECHAZADO'
APROBADOMENORVALOR = 'APROBADO MENOR VALOR'
SINRESPUESTA = 'SIN RESPUESTA'
N/A = 'N/A'
TIPO_RESPUESTA_CLIENTE_CHOICES = (
    (APROBADO, 'APROBADO'),
    (RECHAZADO, 'RECHAZADO'),
    (APROBADOMENORVALOR, 'APROBADO MENOR VALOR'),
    (SINRESPUESTA, 'SIN RESPUESTA'),
    (N/A, 'N/A'),
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
ENPROCESODECOTIZACIONPROVEEDORES = 'EN PROCESO DE COTIZACION PROVEEDORES'
PENDIENTEAPROBACIONCOMPRASCLARO = 'PENDIENTE APROBACION COMPRAS CLARO'
APROBADOCLARO = 'APROBADO CLARO'
PENDIENTEENTREGAPROVEEDOR = 'PENDIENTE ENTREGA PROVEEDOR'
NOAPROBADOPORCOMPRASNOKIAPORMENORVALOR = 'NO APROBADO POR COMPRAS NOKIA POR MENOR VALOR'
PENDIENTEAPROBACIONZONACLARO = 'PENDIENTE APROBACION ZONA CLARO'
PENDIENTEEJECUCION = 'PENDIENTE EJECUCION'
SOLICITUDCANCELADACOMPRAS = 'SOLICITUD CANCELADA COMPRAS'
SOLICITUDCANCELADANOKIAPORMENORVALOR = 'SOLICITUD CANCELADA NOKIA POR MENOR VALOR'
RECIBIDODESUPERVISOR = 'RECIBIDO DE SUPERVISOR'
PENDIENTEPO = 'PENDIENTE PO'
SUMINISTROENIMPORTACION = 'SUMINISTRO EN IMPORTACION'
ENREVISIONANALISTAOFERTASNOKIA = 'EN REVISION ANALISTA OFERTAS NOKIA'
SINPROCESARANALISTA = 'SIN PROCESAR ANALISTA'
EJECUTADONOKIA = 'EJECUTADO NOKIA'
EJECUTADOCLARO = 'EJECUTADO CLARO'
SUBESTADO_OFERTA_CHOICES = (
    (ENPROCESODECOTIZACIONPROVEEDORES, 'EN PROCESO DE COTIZACION PROVEEDORES'),
    (PENDIENTEAPROBACIONCOMPRASCLARO, 'PENDIENTE APROBACION COMPRAS CLARO'),
    (APROBADOCLARO, 'APROBADO CLARO'),
    (PENDIENTEENTREGAPROVEEDOR, 'PENDIENTE ENTREGA PROVEEDOR'),
    (NOAPROBADOPORCOMPRASNOKIAPORMENORVALOR, 'NO APROBADO POR COMPRAS NOKIA POR MENOR VALOR'),
    (PENDIENTEAPROBACIONZONACLARO, 'PENDIENTE APROBACION ZONA CLARO'),
    (PENDIENTEEJECUCION, 'PENDIENTE EJECUCION'),
    (SOLICITUDCANCELADACOMPRAS, 'SOLICITUD CANCELADA COMPRAS'),
    (SOLICITUDCANCELADANOKIAPORMENORVALOR, 'SOLICITUD CANCELADA NOKIA POR MENOR VALOR'),
    (RECIBIDODESUPERVISOR, 'RECIBIDO DE SUPERVISOR'),
    (PENDIENTEPO, 'PENDIENTE PO'),
    (SUMINISTROENIMPORTACION, 'SUMINISTRO EN IMPORTACION'),
    (ENREVISIONANALISTAOFERTASNOKIA, 'EN REVISION ANALISTA OFERTAS NOKIA'),
    (SINPROCESARANALISTA, 'SIN PROCESAR ANALISTA'),
    (EJECUTADONOKIA, 'EJECUTADO NOKIA'),
    (EJECUTADOCLARO, 'EJECUTADO CLARO'),
)

''' ESTADO_OFERTA_CHOICES '''
PENDIENTECOTIZACIONPROVEEDOR = 'PENDIENTE COTIZACION PROVEEDOR'
PENDIENTEAPROBACIONCOMPRASCLARO = 'PENDIENTE APROBACION COMPRAS CLARO'
PENDIENTEEJECUCIONCAMPO = 'PENDIENTE EJECUCION CAMPO'
PENDIENTEENTREGAPROVEEDOR = 'PENDIENTE ENTREGA PROVEEDOR'
PENDIENTEPO = 'PENDIENTE PO'
SINPROCESARANALISTA = 'SIN PROCESAR ANALISTA'
SOLICITUDAPROBADACLARO = 'SOLICITUD APROBADA CLARO'
SOLICITUDAPROBADANOKIAMENORVALOR = 'SOLICITUD APROBADA NOKIA MENOR VALOR'
SOLICITUDCANCELADACOMPRASCLARO = 'SOLICITUD CANCELADA COMPRAS CLARO'
SOLICITUDCANCELADANOKIAPORMENORVALOR = 'SOLICITUD CANCELADA NOKIA POR MENOR VALOR'
PENDIENTEAPROBACIONZONACLARO = 'PENDIENTE APROBACION ZONA CLARO'
EJECUTADONOKIA = 'EJECUTADO NOKIA'
EJECUTADOCLARO = 'EJECUTADO CLARO'
SOLICITUDCANCELADAZONACLARO = 'SOLICITUD CANCELADA ZONA CLARO'
ESTADO_OFERTA_CHOICES = (
    (PENDIENTECOTIZACIONPROVEEDOR, 'PENDIENTE COTIZACION PROVEEDOR'),
    (PENDIENTEAPROBACIONCOMPRASCLARO, 'PENDIENTE APROBACION COMPRAS CLARO'),
    (PENDIENTEEJECUCIONCAMPO, 'PENDIENTE EJECUCION CAMPO'),
    (PENDIENTEENTREGAPROVEEDOR, 'PENDIENTE ENTREGA PROVEEDOR'),
    (PENDIENTEPO, 'PENDIENTE PO'),
    (SINPROCESARANALISTA, 'SIN PROCESAR ANALISTA'),
    (SOLICITUDAPROBADACLARO, 'SOLICITUD APROBADA CLARO'),
    (SOLICITUDAPROBADANOKIAMENORVALOR, 'SOLICITUD APROBADA NOKIA MENOR VALOR'),
    (SOLICITUDCANCELADACOMPRASCLARO, 'SOLICITUD CANCELADA COMPRAS CLARO'),
    (SOLICITUDCANCELADANOKIAPORMENORVALOR, 'SOLICITUD CANCELADA NOKIA POR MENOR VALOR'),
    (PENDIENTEAPROBACIONZONACLARO, 'PENDIENTE APROBACION ZONA CLARO'),
    (EJECUTADONOKIA, 'EJECUTADO NOKIA'),
    (EJECUTADOCLARO, 'EJECUTADO CLARO'),
    (SOLICITUDCANCELADAZONACLARO, 'SOLICITUD CANCELADA ZONA CLARO'),
)
