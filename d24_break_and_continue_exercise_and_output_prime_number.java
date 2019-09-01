public class d24_{
	public static void main(String[] args) {
//		//输出1~100的之间的素数，八个一行
		int flag = 1;
		System.out.print(2 + " ");
		for(int i = 2;i<=100;++i) {
			for(int j = 2;j<i;++j) {
				if(i%j==0) {
					break;
				}
				if(j==i-1) {
					System.out.print(i + " ");
					flag++;
					if (flag%8==0) {
						System.out.print("\n");
					}
				}
				
			}	
		}	
		for1:for(int j = 0;j<3;j++) {//给循环起一个名字
			for2:for(int i=0;i<10;i++) {
				if(i==5) {
					break for1;//我们对指定的名字进行break，如果不写名称，那么默认使用最近的一个循环
				}
				System.out.println("i --->" + i);			
			}
		}
	
		for(int i=1;i<10;i++) {
			if (i == 5) {
				continue;
			}
			System.out.println("i = "+i);
		}
		
	}
}
