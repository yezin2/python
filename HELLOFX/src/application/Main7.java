package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;


public class Main7 extends Application {
	@Override
	public void start(Stage primaryStage) {
		try {
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main7.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			TextField tfI = (TextField)scene.lookup("#tfI");
			TextField tfC = (TextField)scene.lookup("#tfC");
			TextField tfR = (TextField)scene.lookup("#tfR");
			Button btn = (Button) scene.lookup("#sr");
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					String tf1 = tfI.getText();
					String tf2;
					double a = Math.random();
					if(a < 0.33) {
						tf2 = "가위";
					} else if(a > 0.33 && a < 0.66) {
						tf2 = "바위";
					}else {
						tf2 = "보";
					}
					System.out.println("click");
					tfC.setText(tf2);
					
					if(tf1.equals("가위")) {
						if(tf2.equals("가위")) {
							tfR.setText("DRAW--");
						} else if (tf2.equals("바위")) {
							tfR.setText("LOSE...");
						} else if (tf2.equals("보")) {
							tfR.setText("WIN!");
						}
					} else if(tf1.equals("바위")) {
						if(tf2.equals("가위")) {
							tfR.setText("WIN!");
						} else if (tf2.equals("바위")) {
							tfR.setText("DRAW--");
						} else if (tf2.equals("보")) {
							tfR.setText("LOSE...");
						}
					} else if(tf1.equals("보")) {
						if(tf2.equals("가위")) {
							tfR.setText("LOSE...");
						} else if (tf2.equals("바위")) {
							tfR.setText("WIN!");
						} else if (tf2.equals("보")) {
							tfR.setText("DRAW--");
						}
					}
					
				}
			});
			
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
