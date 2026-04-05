---
jira_key: "NBWEB-353"
summary: "Arreglar agente en el el recurso de login de ms-envios"
status: "Finalizada"
type: "Tarea"
priority: "Medium"
assignee: "Emanuel Jesus Ferreyra"
reporter: "Catriel Mercurio"
created: "2022-07-01 11:22"
updated: "2022-07-11 15:44"
labels: []
jira_url: "https://bluinc.atlassian.net/browse/NBWEB-353"
---

# NBWEB-353: Arreglar agente en el el recurso de login de ms-envios

| Campo | Valor |
|-------|-------|
| Estado | Finalizada (Listo) |
| Tipo | Tarea |
| Prioridad | Medium |
| Asignado | Emanuel Jesus Ferreyra |
| Reportado por | Catriel Mercurio |
| Creado | 2022-07-01 11:22 |
| Actualizado | 2022-07-11 15:44 |
| Etiquetas | ninguna |
| Jira | [NBWEB-353](https://bluinc.atlassian.net/browse/NBWEB-353) |

## Descripción

Evitar que se rompa el obtener un token cuando no se encuentra la variable `$u_agent`.

Se debe devolver un objeto tipico para los casos genericos.

```php
<?php

declare(strict_types=1);

namespace App\Service\v1;


use App\Support\TokenManager;
use App\Repository\v1\TokenRepository;

final class TokenService
{
    public function __construct(TokenRepository $tokenRepository)
    {
        $this->tokenRepository = $tokenRepository;
    }

    public function make($user, $data)
    {
        $accessToken = TokenManager::makeToken($user);

        $browser = self::getBrowser();

        $dataAccessToken = [
            'userId'     => $user->id,
            'token'      => $accessToken,
            'ip'         => $_SERVER['REMOTE_ADDR'],
            'user_agent' => $browser['userAgent'],
            'browser'    => $browser['name'],
            'os'         => $browser['platform'],
            'version'    => $browser['version']
        ];

        if ($this->tokenRepository->make($dataAccessToken)) {
            return $accessToken;
        }
    }

    private function getBrowser()
    {
        $u_agent  = $_SERVER['HTTP_USER_AGENT'];
        $bname    = 'Unknown';
        $platform = 'Unknown';
        $version  = "";
        $ub       = "";

	if($u_agent){
        #  First get the platform?
        if (preg_match('/linux/i', $u_agent)) {
            $platform = 'linux';
        } elseif (preg_match('/macintosh|mac os x/i', $u_agent)) {
            $platform = 'mac';
        } elseif (preg_match('/windows|win32/i', $u_agent)) {
            $platform = 'windows';
        }
        

        #  Next get the name of the useragent yes seperately and for good reason
        if (preg_match('/MSIE/i', $u_agent) && !preg_match('/Opera/i', $u_agent)) {
            $bname = 'Internet Explorer';
            $ub = "MSIE";
        } elseif (preg_match('/Firefox/i', $u_agent)) {
            $bname = 'Mozilla Firefox';
            $ub = "Firefox";
        } elseif (preg_match('/Chrome/i', $u_agent)) {
            $bname = 'Google Chrome';
            $ub = "Chrome";
        } elseif (preg_match('/Safari/i', $u_agent)) {
            $bname = 'Apple Safari';
            $ub = "Safari";
        } elseif (preg_match('/Opera/i', $u_agent)) {
            $bname = 'Opera';
            $ub = "Opera";
        } elseif (preg_match('/Netscape/i', $u_agent)) {
            $bname = 'Netscape';
            $ub = "Netscape";
        }
}
        #  finally get the correct version number
        $known = array('Version', $ub, 'other');
        $pattern = '#(?<browser>' . join('|', $known) . ')[/ ]+(?<version>[0-9.|a-zA-Z.]*)#';
        if($u_agent){    if (!preg_match_all($pattern, $u_agent, $matches)) {
            #  we have no matching number just continue
        }}
    

        #  see how many we have
        $i = count($matches['browser']);
        if($u_agent){
        if ($i != 1) {
            # we will have two since we are not using 'other' argument yet
            # see if version is before or after the name
            if (strripos($u_agent, "Version") < strripos($u_agent, $ub)) {
                $version = $matches['version'][0];
            } else {
                $version = $matches['version'][1];
            }
        } else {
            $version = $matches['version'][0];
        }

        #  check if we have a number
        if ($version == null || $version == "") {
            $version = "?";
        }
}
        return array(
            'userAgent' => $u_agent,
            'name'      => $bname,
            'version'   => $version,
            'platform'  => $platform
        );
    }
}
```
