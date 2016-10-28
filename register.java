import java.io.BufferedReader; 
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class register {
	
	public static void main(String arg[]){
		
		HttpURLConnection httpConnect; 
		OutputStream outStream; 
		BufferedReader buffReader; 
		
		try{
			
			URL url = new URL("http://challenge.code2040.org/api/register");
			
			httpConnect = (HttpURLConnection) url.openConnection();
			httpConnect.setDoOutput(true);
			httpConnect.setRequestMethod("POST");
			httpConnect.setRequestProperty("Content-Type", "application/json");
			
			String input = "\"token\":\"0b051b7208115ccaaa141dc3879ec45f\",\"github\":\"https://github.com/k3ne/c2040""; 
			
			System.out.println(input);
			
			outStream = httpConnect.getOutputStream(); 
			outStream.write(input.getBytes());
			outStream.flush(); 
			
			buffReader = new BufferedReader(new InputStreamReader((httpConnect.getInputStream())));
			
			String output; 
			System.out.println("Server Output   \n");
			while((output = buffReader.readLine()) != null){
				System.out.println(output);
			}
			
			httpConnect.disconnect(); 
		}catch (MalformedURLException e){
			e.printStackTrace();
		
		}catch (IOException e){
			e.printStackTrace();
		}
		
	}

}
