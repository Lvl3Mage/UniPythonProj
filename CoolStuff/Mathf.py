class Mathf:
	@staticmethod
	def Clamp(val, _min, _max):
		return max(min(_max, val), _min)
	@staticmethod
	def Lerp(A, B, t):
		return A + (B - A) * Mathf.Clamp(t,0,1)
	@staticmethod
	def LerpUnclamped(A,B,t):
		return A + (B - A) * t