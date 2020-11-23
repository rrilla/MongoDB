package com.example.demo;

import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.core.query.Update;

import com.example.demo.domain.Board;
import com.example.demo.repository.BoardRepository;

import lombok.extern.java.Log;

@Log
@SpringBootTest
public class TestTemplate {

	@Autowired
	MongoTemplate mongoTemplate;
	
	@Test
	public void insertTest() {
		//ArrayList<Board> boards = new ArrayList();
//		Board board1 = new Board(1L, "title1",  "content1", "user");
//		Board board2 = new Board(2L, "title2",  "content2", "user2");
//		Board board3 = new Board(3L, "title3",  "content3", "user3");
		
		//mongoTemplate.insertAll(boards);
//		mongoTemplate.insert(board2);
//		mongoTemplate.insert(board3);
//		log.info("board insert" + board2);
	}
	
	@Test
	public void selectAllTest() {
		List<Board> list = mongoTemplate.findAll(Board.class, "board");
		list.forEach(board -> log.info("board : " + board));
	}
	
	@Test
	public void findCriteriaTest() {	//writer가 user인놈 select
		Criteria criteria = new Criteria("writer");	
		criteria.is("user");
		Query query = new Query(criteria);
		List<Board> list = mongoTemplate.find(query, Board.class, "board");	//마지막 board는 컬렉션명
		list.forEach(board -> log.info("board : " + board));
		//Query query = new Query().addCriteria(Criteria.where("title").is(title));
	}
	
	@Test
	public void updateTest() {
		Criteria criteria = new Criteria("bno");
		criteria.is(1L);
		Query query = new Query(criteria);
		Update update = new Update();
		update.set("title", "수정된 제목임 ㅎ");
		update.set("content", "수정된 내용임 ㅎ");
		mongoTemplate.updateFirst(query, update, Board.class);
		//mongoTemplate.updateMulti(query, update, Board.class);	//여러 행 수정
		//mongoTemplate.updateMulti(new Query(), update, Board.class);	//조건없이 전체 수정
		
		log.info("업뎃 완료~~~~~~~~~~");
	}
	
	@Test
	public void deleteTest() {
		Criteria criteria = new Criteria("writer");
		criteria.is("user");
		
		Query query = new Query(criteria);
		mongoTemplate.remove(query, Board.class);
		//mongoTemplate.remove(new Query(), "board");	//전체삭제
		
		log.info("삭제 완료~~~~~~~~~~");
	}
	
	@Test
	public void countTest() {
		long count = mongoTemplate.count(new Query(), Board.class);
		
		log.info("count : " + count);
	}
	
	BoardRepository boardRepository;
	
}
