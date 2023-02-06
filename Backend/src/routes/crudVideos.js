const router = require("express").Router();
const { Video } = require("../database");
const fs = require('fs');

PATH_FILES_BASE = './uploads/'
PATH_FILES_VIDEO = 'videos/'
PATH_FILES_IMAGE = 'images/'

router
  .route("/allVideos")
  .get((req, res, next) => Promise.resolve()
    .then(() => Video.find({}))
    .then(data => res.status(200).json(data))
    .catch(err => next(err)))

router
  .route("/createVideo")
  .post((req, res, next) => Promise.resolve()
    .then(() => { 
      path_video = `${PATH_FILES_VIDEO}${req.files.video.name}`
      path_tumb = `${PATH_FILES_IMAGE}${req.files.thumbnail.name}`

      var body = JSON.parse(req.files.body.data.toString())

      // save video
      fs.writeFile(PATH_FILES_BASE + path_video, req.files.video.data, (err) => {
        if (err) throw err;
      }); 

      // save image
      fs.writeFile(PATH_FILES_BASE + path_tumb, req.files.thumbnail.data, (err) => {
        if (err) throw err;
      });

      new Video({ ...body, video: path_video, thumbnail: path_tumb}).save()
        .then(() => res.status(201).json({ message: `Video created` }))
        .catch(err => next(err))

    })
  )


module.exports = router