## Task 1 Ansible - 28 November 2023

### 1. Buat inventory
```yaml
all:
  hosts:
    btj-academy:
      ansible_host: 10.184.0.100
```
### 2. Buatlah playbook dengan perintah untuk menjalankan docker container
```yaml
- name: Task 1 Ansible - Daffa
  hosts: btj-academy
  become: true
  tasks:
    - docker_container:
        name: "daffa"
        image: "todo-list-app:v1.0"
        interactive: true
        tty: true
        ports:
          - "9999:9999"
```

### Jalankan ansible
1. Copy ssh dari local ke VM
```bash
scp C:\Users\USER\.ssh\id_rsa <user>@btj-academy.bangunindo.io:/home/<user>/.ssh/id_rsa
```
2. Buat dockerfile di lo=kal untuk ansible di direktori yang sama yaitu `inventory.yaml` and `playbook.yaml`
```dockerfile
FROM python:3.9-alpine

RUN apk update && apk add build-base libffi-dev

RUN pip3 install ansible

COPY . .
```
3. Build docker image untuk lokal dan jalankan image sebagai container
```bash
docker build -t ansible .
docker run -it -d -v C:/Users/daffa\.ssh\:/root/.ssh/ --name ansible1 ansible
```
4. Masuk ke container yang sudah di-run, lalu install openssh di dan ubah izin untuk ssh key
```bash
docker exec -it ansible1 sh
apk add openssh
chmod -R 400 /root/.ssh/id_rsa*
```
5. Jalankan ansible
```bash
ansible-playbook -i inventory.yaml playbook.yaml --user daffadamarardhika
```
6. Masuk ke SSH dan verifikasi container sudah dijalankan atau belum
```bash
ssh daffadamarardhika@btj-academy.bangunindo.io
docker ps -a
```