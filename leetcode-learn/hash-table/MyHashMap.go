// Design a HashMap without using any built-in hash table libraries.

type MyHashMap struct {
	bucket []int
}

func Constructor() MyHashMap {
	b := make([]int, 1000001)
	for i, _ := range b {
		b[i] = -1
	}
	return MyHashMap{bucket: b}
}

func (this *MyHashMap) Put(key int, value int) {
	this.bucket[key] = value
}

func (this *MyHashMap) Get(key int) int {
	return this.bucket[key]
}

func (this *MyHashMap) Remove(key int) {
	this.bucket[key] = -1
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */