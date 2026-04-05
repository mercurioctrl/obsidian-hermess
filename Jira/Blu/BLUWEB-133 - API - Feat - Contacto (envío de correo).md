---
jira_key: "BLUWEB-133"
aliases: ["BLUWEB-133"]
summary: "API - Feat - Contacto (envío de correo)"
status: "LISTO"
type: "Subtarea"
priority: "High"
assignee: "Ezequiel manzano"
reporter: "Catriel Mercurio"
created: "2025-08-20 09:43"
updated: "2025-08-20 20:15"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/BLUWEB-133"
---

# BLUWEB-133: API - Feat - Contacto (envío de correo)

| Campo | Valor |
|-------|-------|
| Estado | LISTO (Listo) |
| Tipo | Subtarea |
| Prioridad | High |
| Asignado | Ezequiel manzano |
| Reportado por | Catriel Mercurio |
| Creado | 2025-08-20 09:43 |
| Actualizado | 2025-08-20 20:15 |
| Etiquetas | ninguna |
| Jira | [BLUWEB-133](https://bluinc.atlassian.net/browse/BLUWEB-133) |

## Relaciones

- **Padre:** [[BLUWEB-13 - Sitio Web_Etapa 0|BLUWEB-13]] Sitio Web_Etapa 0
- **has action item:** [[BLUWEB-130 - APP - Refactor - Seccion contacto v2 con calendario de citas|BLUWEB-130]] APP - Refactor - Seccion contacto v2 con calendario de citas

## Descripcion

Usando la misma configuraron de correo utilizada para las citas , agregaremos un recurso para el formulario de contacto tradicional que recibe un payload del front del siguiente tipo

```
POST {API_URL}/api/contact
```

```
{
    "name": "marbe",
    "lastName": "moreno",
    "email": "marbem1995@gmail.com",
    "company": "sadsd",
    "interest": "it",
    "message": "Esto es una prueba ",
    "recaptchaToken": "0cAFcWeA7-ALGZe0wrG7E6u2MGwJ8_SWtbdRPjwV4NWEWXS-ru_YF94GyBKsMWWagN-iPkO2GUH4K_MoG_GQlpoTjw2McRz1CZR_lB6D7LGytf3chLn4EFliwOTJL9gJrZYkonFv7SMeit2KPUT7RLZJLV1x-5yMdId-WrcHYJiownP0jPw1w9zxy2B3s4WqRFrTa68KxaUtv23O05EQyJNms9q4TmpY4J-EAwpFTsknS34cCnIPgue6aG3Eh3xOA6GM8Kha4x_KWSYJdyq7DYWUSJNbLX43MEm2rvt4vEU96_nL3VWFOmRscT8aAqIlEsVx1vju-DNVizHkIkWP6MHCaIK_1eUR-r0eKFDAoj9m4qiww5GpHj1G10v8bh-JdcIDIrEeIQC5Zdoc-tZKi0G6ZMKHQ0LSUL0RNWipGoAU3GUuFAuxg3qocwb_DSwevEtTBYc-pEPgAC5jqu4McXaEKiZIpDzlUOu42X9Mj8g9_zU8Lq8fkxw8wfpke9Obl0hnHTaRbGLWGp-iitkUb1nNwq3KVFfG-EbEpxFunXLnF4hBd0EcWqyPDR_Gs-1gZP1B9ozx-BzRpkezBvmbQyB4LRXkKuabUJo4RhoYSw3YegBVV_QcWa7xds5Jl2WeVGDeXcyywE5D0hpQykZPcqu5tU_D9_CrBR-qGbEEAixsNn77ilWHI_wNKw3jonTAfErILdgxg_J6OM51SKx-MJZ-wpOzCscZ91p-haPpkUyOd-CUhupMyQeqBy5Z9hv8aGKO4QiO_MKqJAFKtd9bbH2KwTigCiGxyY-ho8EUVUczyYatb31anT4UmtkzeAK2PTEgUi8MZPZf7iHjcLFm1NSq_WwjvJEiE_ZmLUkELLmq6IZXi3JbJNrtW2SoTUdshfWZrFaDpqg6J-MMh9F5sfhRzDLSXQ3wovnTgwJwfh1gbXM_5QniXrSpyNYdeQlJYumwfcs5bfqFKB0siBCVZmTQrOHQOOie8wT7XQHRwa7hNZWdGr6leXNUFp61F4k7FcGEZAzmVm9Jrrt6CBk5_sXX2KaWQUCNx7M6sUKqZuBCISKq_oCJLshXAfhhYTYFuari0ETkl3VRxSBjxApadiM-3_ttGdOSMRpRG8Ck9h31L-Uayd8T8NoHMl1S4EESazcy6AQmxaDYoNNWvNIJ5yzw7kDAYVPb050d_roqNqyU_bkkFFadEihQg7HR5tdE0jqtKAg6gVfULBIKE_EulkuZSE0c6Z--yoVJObCSueDgWQaqBu8yU5HSLsGjlLAohDNgZUtr58I9gPGFDl4VhR4d0VgkyvZmlp4rcqoohu1W4ZPQR1-CbgtCcPuzxUpGyefMvU3sMiTIg3EC56lhGctHlPuwMUZZmOi7iTVapcoZevq9Z2ZvqNzrWlxQAMGNMADX-BGQ9e-s9_O0e9Obw6gvsFp9pVJvJODTkRmuaQ_ERXZ09E6NPariO2fs4ZMSpu-Y6ltYPmPfDAL_RLusIqLso__becTSXtlKtXEgIIhLLLOJmDh-XT0ZffD5xTdx0ciKo1t3g43skgZgDkyFa7MtkkSX5qIkyGAg"
}
```
