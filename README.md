# Image Asciify Service
Use fastapi to construct endpoints. Refactor PyWhatKit image_to_ascii_art method to convert uploaded png file into ascii arc text files.
https://github.com/Ankit404butfound/PyWhatKit

## Apis docs url
http://localhost:8088/docs

### Create Ascii Art File
```bash
$ curl -F "png=@dove.png" localhost:8088/images
```

### Get ascii text by using image_id
```bash
$ curl localhost:8088/images/{image_id}
```

### List all image ids
```bash
$ curl localhost:8088/images
$ curl "localhost:8088/images?limit=3"
```