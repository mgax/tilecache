from TileCache.Cache import Cache

class Null(Cache):

    def getKey(self, tile):
        return "/".join(map(str, [tile.layer.name, tile.x, tile.y, tile.z]))

    def get(self, tile):
        return None

    def set(self, tile, data):
        return data

    def delete(self, tile):
        pass

    def attemptLock(self, tile):
        return True

    def unlock(self, tile):
        pass
