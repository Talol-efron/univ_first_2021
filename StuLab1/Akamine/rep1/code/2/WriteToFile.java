import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class WriteToFile
{
    public static void main(String[] args)
    {
        try{
            File f = new File("out_java.txt");
            FileWriter writer = new FileWriter(f);
            
            for(int i=0; i<1000*1000*10; ++i) {
                writer.write(String.valueOf(i));
            }
            
            writer.close();
        }catch(IOException e) {
            System.out.println(e);
        }
    }
}
