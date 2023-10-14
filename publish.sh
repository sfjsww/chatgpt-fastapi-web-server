## mac m1
docker buildx build -t hub.fuxi.netease.com/ai-project/art-aop:test . --platform=linux/amd64
## ubu
# docker build -t hub.fuxi.netease.com/ai-project/art-aop:test .
docker push hub.fuxi.netease.com/ai-project/art-aop:test