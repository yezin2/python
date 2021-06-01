package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;


public class Main9 extends Application {
	String callNum = "";
	@Override
	public void start(Stage primaryStage) {
		try {
			Alert alert = new Alert(AlertType.INFORMATION);
			AnchorPane root = (AnchorPane)FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
			
			TextField tfNum = (TextField)scene.lookup("#tfNum");
			Button btn1 = (Button) scene.lookup("#btn1");
			Button btn2 = (Button) scene.lookup("#btn2");
			Button btn3 = (Button) scene.lookup("#btn3");
			Button btn4 = (Button) scene.lookup("#btn4");
			Button btn5 = (Button) scene.lookup("#btn5");
			Button btn6 = (Button) scene.lookup("#btn6");
			Button btn7 = (Button) scene.lookup("#btn7");
			Button btn8 = (Button) scene.lookup("#btn8");
			Button btn9 = (Button) scene.lookup("#btn9");
			Button btn0 = (Button) scene.lookup("#btn0");
			Button btnCall = (Button) scene.lookup("#btnCall");
			
			btn0.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn0.getText();
					tfNum.setText(callNum);
				}
			});
			btn1.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn1.getText();
					tfNum.setText(callNum);
				}
			});
			btn2.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn2.getText();
					tfNum.setText(callNum);
				}
			});
			btn3.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn3.getText();
					tfNum.setText(callNum);
				}
			});
			btn4.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn4.getText();
					tfNum.setText(callNum);
				}
			});
			btn5.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn5.getText();
					tfNum.setText(callNum);
				}
			});
			btn6.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn6.getText();
					tfNum.setText(callNum);
				}
			});
			btn7.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn7.getText();
					tfNum.setText(callNum);
				}
			});
			btn8.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn8.getText();
					tfNum.setText(callNum);
				}
			});
			btn9.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					callNum += btn9.getText();
					tfNum.setText(callNum);
				}
			});
			
			btnCall.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					alert.setTitle("Calling...");
					alert.setHeaderText(callNum + "로 전화거는 중");
					alert.setContentText("확인 버튼을 누르면 꺼집니다.");
					
					alert.showAndWait();
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
