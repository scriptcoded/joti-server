const express = require('express')
const cors = require('cors')
const { exec } = require('child_process')
const fs = require('fs')

const app = express()

app.use(cors())
app.use(express.json())

app.post('/', (req, res, next) => {
  fs.writeFile('tmp.py', req.body.script, (err) => {
    if (err) {
      res.send({
        error: err
      })
      return
    }

    exec('python3 pyboard.py tmp.py', (err) => {
    if (err) {
        res.send({
          error: err
        })
        return
      }

      res.send({
        ok: true
      })
    })
  })


  // let commands = req.body.script
  //   .replace(/\n+/g, '\n')
  //   .split('\n')
  //   .join(' ~ ')

  // let stdout = ''
  // let stderr = ''

  // commands = `~ ${commands} ~`

  // const cmd = spawn('rshell', [
  //   'repl',
  //   commands
  // ])

  // cmd.stdout.on('data', (data) => {
  //   stdout += `${data}`
  //   console.log(`stdout: ${data}`);
  // });
  
  // cmd.stderr.on('data', (data) => {
  //   stderr += `${data}`
  //   console.error(`stderr: ${data}`);
  // });

  // cmd.on('close', (code) => {
  //   console.log('Hi')
  //   res.send({
  //     stdout,
  //     stderr,
  //     ok: true
  //   })
  // })
})

app.listen(4000, () => {
  console.log('Server running on port 4000');
})
