#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from fastapi import FastAPI, status
from typing import List

from info.catcher import weather, usdXbrl, btcXbrl, lottery

app= FastAPI(title="API do Nelson", version=1.0)

@app.get("/", status_code= status.HTTP_200_OK)
def wellcome():
    """
    First page, returns all info at once without soting.

    Página principal, retorna todas as informações sem filtros.
    """

    info= {
            "tempo": weather(),
            "Dólar": usdXbrl(),
            "Bitcoin": btcXbrl(),
            "Mega Sena": lottery()
    }

    return info

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
