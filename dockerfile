# 1. Python imajı al
FROM python:3.10-slim

# 2. Çalışma klasörünü oluştur
WORKDIR /app

# 3. Gerekli dosyaları kopyala
COPY . .
COPY requirements.txt requirements.txt
# 4. Kütüphaneleri kur

#RUN RUN pip3 install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org -r requirements.txt
RUN pip install --no-cache-dir \
    --trusted-host pypi.org \
    --trusted-host files.pythonhosted.org \
    -r requirements.txt


# pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8000
# 5. Uygulamayı başlat
CMD ["uvicorn", "main:app"]


