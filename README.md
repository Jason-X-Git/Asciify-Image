# Image Asciify Service
Use fastapi to construct endpoints. The uploaded png file will be converted ascii art text, and saved as txt file in the sub folder "asciify_texts". Refactor PyWhatKit image_to_ascii_art method to convert uploaded png file into ascii art text.
https://github.com/Ankit404butfound/PyWhatKit

## Start service using make commands included in Makefile
* `make build` to build a Docker container
* `make service` to start the service on port 8088
* `make test` to run tests
 
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

## Next Implementation
* Use Gunicorn add more workers, or cloud scaling to handle more requests.
* Limit upload PNG file size.
* Improve algorithm of asciify to make better-quality ascii art text.
* Add better caching support.
* Use memory database such as Redis to replace local folder storage.