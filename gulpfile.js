const gulp = require('gulp');
const util = require('gulp-util')
const gulpConnect = require('gulp-connect');
const connect = require('connect');
const cors = require('cors');
const path = require('path');
const exec = require('child_process').exec;
const portfinder = require('portfinder');

const DIST_DIR = 'web_deploy';

gulp.task('build', function (cb) {
  exec('npm run build', function (err, stdout, stderr) {
    console.log(stderr);
    cb(err);
  });
});

gulp.task('reload', gulp.series('build'), function () {
  gulp.src(DIST_DIR).pipe(gulpConnect.reload())
});

gulp.task('watch', function () {
  gulp.watch(['spec/**/*', 'web/**/*'], gulp.series('reload'));
});

gulp.task('serve', gulp.parallel('build', 'watch', function() {
  portfinder.getPort({ port: process.env.PORT_REDOC || 5000 }, function (err, port) {
    gulpConnect.server({
      root: [DIST_DIR],
      livereload: true,
      port: port,
      middleware: function (gulpConnect, opt) {
        return [
          cors()
        ]
      }
    });
  });
}));