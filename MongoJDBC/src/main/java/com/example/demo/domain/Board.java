package com.example.demo.domain;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "board")	//몽고db의 컬렉션명을 써서 연결
public class Board {

	@Id
	private String bno;
	private String title;
	private String content;
	private String writer;
	
}
