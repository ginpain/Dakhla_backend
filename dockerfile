# ── Base image ────────────────────────────────────────────────────────────────
FROM python:3.12-slim

# ── OS dependencies ───────────────────────────────────────────────────────────
# gdal-bin → command-line tools
# libgdal32 → shared library that Python will link to
# libgeos3 / libproj22 → required by GDAL’s vector/CRS features
# build-essential / gcc → compile Python bindings during `pip install`
RUN apt-get update && apt-get install -y --no-install-recommends \
        gdal-bin libgdal-dev libgeos-dev libproj-dev \
        build-essential gcc && \
    rm -rf /var/lib/apt/lists/*


# Tell pip where the GDAL headers live for the build step
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal \
    C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

# ── Python dependencies ───────────────────────────────────────────────────────
# Pin GDAL at the same version as your Windows wheel.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# In requirements.txt add a line:  gdal==3.8.4

# ── Project code ─────────────────────────────────────────────────────────────
COPY . .

# Optional: collect static files during build
#RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
