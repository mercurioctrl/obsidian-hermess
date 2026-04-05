---
jira_key: "LIO-345"
aliases: ["LIO-345"]
summary: "APP - Feat - Agregar codigo de trackeo de evento aportado por LEO para adwords"
status: "Finalizada"
type: "Subtarea"
priority: "Medium"
assignee: "Marbe Moreno"
reporter: "Catriel Mercurio"
created: "2025-05-12 12:08"
updated: "2025-05-13 16:04"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/LIO-345"
---

# LIO-345: APP - Feat - Agregar codigo de trackeo de evento aportado por LEO para adwords

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Subtarea |
| Prioridad | Medium |
| Asignado | Marbe Moreno |
| Reportado por | Catriel Mercurio |
| Creado | 2025-05-12 12:08 |
| Actualizado | 2025-05-13 16:04 |
| Etiquetas | ninguna |
| Jira | [LIO-345](https://bluinc.atlassian.net/browse/LIO-345) |

## Relaciones

- **Padre:** [[LIO-344]] Adwords y Analytics

## Descripcion

Buscaremos la forma de agregarlo para impedir que bloquee el renderizado (luego buscaremos variables menos intrusivas)

```
<script>
(function() {
	var xhrSend = window.XMLHttpRequest.prototype.send;
	window.XMLHttpRequest.prototype.send = function() {
		var xhr = this;
		var intervalId = window.setInterval(function() {
			if(xhr.readyState != 4) {
				return;
			}
			dataLayer.push({
				'event': 'ajaxSuccess',
				'eventCategory': 'AJAX',
				'eventAction': xhr.responseURL,
				'eventLabel': xhr.responseText
			});
			clearInterval(intervalId);
		}, 1);
		return xhrSend.apply(this, [].slice.call(arguments));
	};
})();
</script>
```
