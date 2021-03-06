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
RURAL4X4 = 'RURAL 4X4'
TIPO_ACCESO_CHOICES = (
    (URBANO, 'URBANO'),
    (ACCESODIFICIL, 'ACCESO DIFICIL'),
    (FLUVIAL, 'FLUVIAL'),
    (AEREO, 'AEREO'),
    (COMUNIDADINDIGENA, 'COMUNIDAD INDIGENA'),
    (PALABRERO, 'PALABRERO'),
    (RURAL4X4, 'RURAL 4X4'),
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
NA = 'N/A'
TIPO_ELEMENTO_CHOICES = (
    (CAPEX, 'CAPEX'),
    (OPEX, 'OPEX'),
    (NA, 'N/A'),
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
BODEGANOKIA = 'BODEGA NOKIA'
BODEGACLARO = 'BODEGA CLARO'
COMPRALOCAL = 'COMPRA LOCAL'
INTERMEDIARIO = 'INTERMEDIARIO'
PALABRERO = 'PALABRERO'
SUMINISTRADOCLIENTE = 'SUMINISTRADO CLIENTE'
NA = 'N/A'
TIPO_ADQUISICION_CHOICES = (
    (PROVEEDOR, 'PROVEEDOR'),
    (PERSONALNOKIA, 'PERSONAL NOKIA'),
    (BODEGANOKIA, 'BODEGA NOKIA'),
    (BODEGACLARO, 'BODEGA CLARO'),
    (COMPRALOCAL, 'COMPRA LOCAL'),
    (INTERMEDIARIO, 'INTERMEDIARIO'),
    (PALABRERO, 'PALABRERO'),
    (SUMINISTRADOCLIENTE, 'SUMINISTRADO CLIENTE'),
    (NA, 'N/A'),
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
SUMA = 'SUMA'
NA = 'N/A'
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
    (SUMA, 'SUMA'),
    (NA, 'N/A'),
)

''' TIPO_RESPUESTA_CLIENTE_CHOICES '''
APROBADO = 'APROBADO'
RECHAZADO = 'RECHAZADO'
APROBADOMENORVALOR = 'APROBADO MENOR VALOR'
SINRESPUESTA = 'SIN RESPUESTA'
NOAPLICA = 'N/A'
TIPO_RESPUESTA_CLIENTE_CHOICES = (
    (APROBADO, 'APROBADO'),
    (RECHAZADO, 'RECHAZADO'),
    (APROBADOMENORVALOR, 'APROBADO MENOR VALOR'),
    (SINRESPUESTA, 'SIN RESPUESTA'),
    (NOAPLICA, 'N/A'),
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
