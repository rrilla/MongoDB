package mongo;


import org.bson.Document;

import com.mongodb.BasicDBObject;
import com.mongodb.MongoClient;
import com.mongodb.client.FindIterable;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;

public class MongoJDBC {
	
	private static MongoDatabase db;
	private static MongoClient mongoClient;
	private static MongoCollection<Document> collection;
	
	private static void findTest() {
		BasicDBObject inQuery = new BasicDBObject();
		inQuery.put("deptno", 20);
		
		MongoCollection<Document> collection = db.getCollection("employees");
		MongoCursor<Document> cursor = collection.find().iterator();
		
		while(cursor.hasNext()) {
			Document doc = cursor.next();
			System.out.println(doc.toJson());
		}
		
//		for(Document doc : collection.find()) {
//			System.out.println(doc.toJson());
//		}
	}
	
	private static void insertTest() {
		Document doc = new Document("empno", 9000)
				.append("ename", "kim")
				.append("job", "salesman")
				.append("sal", 4000)
				.append("deptno", 4);
		
		collection.insertOne(doc);
	}
	
	private static void updateTest() {
		BasicDBObject inQuery = new BasicDBObject();
		inQuery.put("empno", 9000);
		
		BasicDBObject newQuery = new BasicDBObject()
				.append(
						"$set",
						new BasicDBObject("ename", 1541)
						.append("job", "gamer"));
		collection.updateOne(inQuery, newQuery);
	}
	
	private static void deleteTest() {
		BasicDBObject inQuery = new BasicDBObject();
		inQuery.put("ename", "SMITH");
		
		collection.deleteOne(inQuery);
	}
	
	
	
	public static void main(String[] args) {
		
		mongoClient = new MongoClient( "localhost" , 27017 );
		db = mongoClient.getDatabase("test");
		collection = db.getCollection("employees");
		
		deleteTest();
		findTest();
		//updateTest();
		
		
		
//		BasicDBObject inquery = new BasicDBObject();
//		inquery.put("deptno", 30);
//		FindIterable<Document> iterate = collection.find(inquery);
//		System.out.println(iterate.toString());
		
	}
}
