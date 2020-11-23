package com.example.demo.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.example.demo.domain.Board;

public interface BoardRepository extends MongoRepository<Board, Long>{

}
