---
jira_key: "PED-20"
summary: "API - Feat - Obtener informacion completa cliente"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2023-08-08 08:30"
updated: "2023-08-09 11:17"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/PED-20"
---

# PED-20: API - Feat - Obtener informacion completa cliente

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2023-08-08 08:30 |
| Actualizado | 2023-08-09 11:17 |
| Etiquetas | ninguna |
| Jira | [PED-20](https://bluinc.atlassian.net/browse/PED-20) |

## Descripción

Este repositorio trae la informacion completa del cliente, sirve para completar el formulario de edición de los datos del cliente y ademas para cualquier otro fin que se requiera consultar informacion especifica o contener cualquier parámetro del cliente que no tiene otro lugar

```
GET {API_URL}/v1/clients/{id del cliente}
```

```
{
    "clientCode": "024865",
    "clientName": "COLONEL CLAUDIO LIVIO",
    "commercialName": "Mercurio",
    "clientAddress": "ANDRES FERREYRA 2685",
    "clientCity": "",
    "cityCode": "3678",
    "postalCode": "1678",
    "phone1": "011-4759-951",
    "phone2": "011-4759-951",
    "fax": "",
    "taxId": "20-13131339-0",
    "contactName": "Claudio ",
    "bankName": "",
    "bankAddress": "",
    "bankCity": "",
    "bankProvince": "0",
    "bankEntity": "",
    "bankAgency": "",
    "bankAccount": "",
    "clientObservations": "",
    "paymentCode": "CO",
    "paymentDay1": "0",
    "paymentDay2": "0",
    "agentCode": "36",
    "discount": "1",
    "paymentDiscount": ".00",
    "overdue": ".000",
    "risk": ".000",
    "invoiceCopies": "1",
    "rapCode": "",
    "invoiceSeries": "A",
    "tariffCode": "",
    "taxId": "6",
    "requires": "0",
    "subAccount": "",
    "salesAccount": "",
    "wholesaler": "0",
    "select": "0",
    "creditRisk": ".000",
    "labelCount": "1",
    "addressDirection": "0",
    "email": "mercurioweb@yahoo.com.ar",
    "password": "",
    "birthCountry": "ARGE",
    "bankCountry": "ARGE",
    "groupCode": "04",
    "currencyDivision": "DOL",
    "transportCode": "",
    "taxIdentificationNumber": "",
    "insuredLimit": "0",
    "taxCode": "",
    "municipalInsurance": "",
    "retailTariff": "1",
    "wholesaleTariff": "1",
    "group": "0",
    "advances": ".000",
    "advanceAccount": "",
    "withholdingTax": "0",
    "identityDocument": "1",
    "initialBalance": ".000",
    "vatSubscriber": "1",
    "inactive": "0",
    "website": "0",
    "clientId": "24865",
    "postalCodeId": null,
    "countryId": "7",
    "cityId": "3681",
    "provinceId": "2",
    "clientGroupId": "17",
    "salespersonId": "36",
    "paymentMethodId": "1",
    "currencyId": "1",
    "registrationDate": "2014-10-14 08:52:14.103",
    "paymentMethodCode": null,
    "verified": "1",
    "web": "---",
    "rmaEmail": null,
    "specialOfferDiscount": "50.00000",
    "intermediation": null,
    "lastPurchase": null,
    "generalDiscount": null,
    "lastSalesperson": "1",
    "salespersonChangeDate": "2017-10-23 06:10:17.297",
    "manualPrice": "0",
    "profile": "1",
    "perception": ".00000",
    "perceptionExpiry": "2023-06-01 00:00:00.000",
    "companyCode": "5",
    "belongsCompany": null,
    "excludePerception": "1",
    "specialPrice": null,
    "clientLo": null,
    "specialPriceFromCost": null,
    "productecaId": null
}
```

Repositorios útiles

```
SELECT TOP (1000) 
    [ccodcli] AS clientCode,
    [cnomcli] AS clientName,
    [cnomcom] AS commercialName,
    [cdircli] AS clientAddress,
    [cpobcli] AS clientCity,
    [ccodpobl] AS cityCode,
    [cptlcli] AS postalCode,
    [ctfo1cli] AS phone1,
    [ctfo2cli] AS phone2,
    [cfaxcli] AS fax,
    [cdnicif] AS taxId,
    [ccontacto] AS contactName,
    [cnbrbco] AS bankName,
    [cdirbco] AS bankAddress,
    [cpobbco] AS bankCity,
    [cprovbco] AS bankProvince,
    [centidad] AS bankEntity,
    [cagencia] AS bankAgency,
    [ccuenta] AS bankAccount,
    [cobscli] AS clientObservations,
    [ccodpago] AS paymentCode,
    [ndia1pago] AS paymentDay1,
    [ndia2pago] AS paymentDay2,
    [ccodage] AS agentCode,
    [ndto] AS discount,
    [ndpp] AS paymentDiscount,
    [nmorosos] AS overdue,
    [nriesgo] AS risk,
    [ncopfac] AS invoiceCopies,
    [ccodrap] AS rapCode,
    [cseriefact] AS invoiceSeries,
    [cctarem] AS tariffCode,
    [niva] AS taxId,
    [lreq] AS requires,
    [csubcta] AS subAccount,
    [cctavtas] AS salesAccount,
    [lmayorista] AS wholesaler,
    [lselect] AS select,
    [nriesgoalc] AS creditRisk,
    [netiquetas] AS labelCount,
    [cdireccion] AS addressDirection,
    [email] AS email,
    [password] AS password,
    [cnaccli] AS birthCountry,
    [cnacbco] AS bankCountry,
    [ccodgrup] AS groupCode,
    [ccoddiv] AS currencyDivision,
    [ccodtrans] AS transportCode,
    [ccuit] AS taxIdentificationNumber,
    [limpins] AS insuredLimit,
    [ccodib] AS taxCode,
    [cinscmun] AS municipalInsurance,
    [ntarifapp] AS retailTariff,
    [ntarifamay] AS wholesaleTariff,
    [lagrupar] AS group,
    [nanticipos] AS advances,
    [csctaant] AS advanceAccount,
    [lpercep] AS withholdingTax,
    [ndocidenti] AS identityDocument,
    [nsaldoini] AS initialBalance,
    [nsubri] AS vatSubscriber,
    [inactivo] AS inactive,
    [sitio] AS website,
    [ID_CLIENTE] AS clientId,
    [Id_CodigoPostal] AS postalCodeId,
    [ID_PAIS] AS countryId,
    [ID_CIUDAD] AS cityId,
    [ID_PROVINCIA] AS provinceId,
    [ID_GRUPOCLIENTE] AS clientGroupId,
    [ID_VENDEDOR] AS salespersonId,
    [ID_FORMAPAGO] AS paymentMethodId,
    [ID_DIVISA] AS currencyId,
    [FECHA_ALTA] AS registrationDate,
    [codigoFP] AS paymentMethodCode,
    [verificado] AS verified,
    [www] AS web,
    [EMAILRMA] AS rmaEmail,
    [superOfertaDto] AS specialOfferDiscount,
    [intermediacion] AS intermediation,
    [ULTIMA_COMPRA] AS lastPurchase,
    [dtoGral] AS generalDiscount,
    [ULTIMO_VENDEDOR] AS lastSalesperson,
    [FECHA_CAMBIO_VENDEDOR] AS salespersonChangeDate,
    [precioAMano] AS manualPrice,
    [perfil] AS profile,
    [percepcion] AS perception,
    [percepcion_vencimiento] AS perceptionExpiry,
    [CODEMP] AS companyCode,
    [perteneceEmpresa] AS belongsCompany,
    [excluirPercepcion] AS excludePerception,
    [specialPrice] AS specialPrice,
    [clientLo] AS clientLo,
    [specialPriceFromCost] AS specialPriceFromCost,
    [productecaId] AS productecaId
FROM [NewBytes_DBF].[dbo].[clientes]

```
