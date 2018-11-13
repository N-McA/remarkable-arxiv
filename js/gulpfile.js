
const gulp = require('gulp');
const replace = require('gulp-replace')
const terser = require('gulp-terser');
const pump = require('pump');
const fs = require('fs')

const DIST = 'dist'

gulp.task('minify', () => {
  return pump([
    gulp.src('src/bookmarklet.js'),
    terser(),
    gulp.dest(DIST),
  ])
})


gulp.task('test-page', ['minify'], () => {
  let js = fs.readFileSync('dist/bookmarklet.js', 'utf8')
  let jsEncoded = encodeURIComponent(js)
  return gulp.src('src/test-page.html')
    .pipe(replace('REPLACED_BY_BOOKMARKLET_CODE', jsEncoded))
    .pipe(gulp.dest(DIST))
})


gulp.task('default', ['test-page'])
