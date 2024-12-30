// Design a HashSet without using any built-in hash table libraries.

type MyHashSet struct {
	bucket []bool
}

func Constructor() MyHashSet {
	bucket := make([]bool, 1000001)
	return MyHashSet{bucket: bucket}
}

func (this *MyHashSet) Add(key int) {
	this.bucket[key] = true
}

func (this *MyHashSet) Remove(key int) {
	this.bucket[key] = false
}

func (this *MyHashSet) Contains(key int) bool {
	if this.bucket[key] {
		return true
	}
	return false
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */