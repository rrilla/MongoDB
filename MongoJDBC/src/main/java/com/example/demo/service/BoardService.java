package com.example.demo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Service;

import com.example.demo.domain.Board;

@Service
public class BoardService {

	@Autowired
	MongoTemplate mongoTemplate;
	
	public List<Board> main(){
		return mongoTemplate.findAll(Board.class, "board");
	}
	
	public void register(Board board) {
		mongoTemplate.insert(board);
	}
	
	public Board detail(String id) {
//		Criteria criteria = new Criteria("bno");
//		criteria.is(id);
//		Query query = new Query(criteria);
		return mongoTemplate.findById(id, Board.class);
	}
}
