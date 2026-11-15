import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'

const page = await readFile(new URL('./index.html', import.meta.url))
const port = Number(process.env.RADAR_PORT || 4173)
createServer((request, response) => {
  if (!['GET', 'HEAD'].includes(request.method) || !['/', '/index.html'].includes(request.url)) {
    response.writeHead(404).end()
    return
  }
  response.writeHead(200, {
    'Content-Type': 'text/html; charset=utf-8',
    'X-Content-Type-Options': 'nosniff'
  })
  response.end(request.method === 'HEAD' ? undefined : page)
}).listen(port, '127.0.0.1', () => console.log('LAMTORRO Business Radar → http://127.0.0.1:' + port))
