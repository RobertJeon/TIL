public delegate void MyDelegate(string message);

public class MyClass
{
    public void MyMethod(string message)
    {
        Console.WriteLine("MyMethod 호출: " + message);
    }
}

class Program
{
    static void Main()
    {
        // 델리게이트 인스턴스 생성
        MyDelegate myDelegate = new MyDelegate(new MyClass().MyMethod);

        // 델리게이트를 통한 메서드 호출
        myDelegate("안녕하세요!");
    }
}